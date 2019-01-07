from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post

from .forms import PostForm
from .forms import JoinForm


from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
# Create your views here.



@login_required(login_url="/login")
def post(request):  #게시글 출력
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/post.html' , context)


@login_required(login_url="/login")
def test(request):   #게시글 쓰기
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) #commit = False 뜻은 DB에 바로 저장 안한다. 
            instance.user =  request.user
            instance.save()
        return redirect('post')
    else:
        form=PostForm()
        return render(request,'blog/test.html',{'form':form})

@login_required(login_url="/login")
def edit(request,pk):
    template = 'blog/test.html'
    post = get_object_or_404(Post , pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance =post)
        if form.is_valid():
            if post.user == User.objects.get(username = request.user.get_username()):
                form.save()
            else:
                return HttpResponse('권한이 없습니다.')
    else:
        form = PostForm(instance = post)
    context = {
        'form':form,
        'post':post,
    }
    return render(request,template,context)



@login_required(login_url="/login")
def index(request,pk):  #게시글 번호및 내용
    posts = Post.objects.filter(pk=pk)
    context = {'posts':posts}
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/index.html',context)



@login_required(login_url="/login")
def delete(request,pk):   #게시글 삭제
    post =  Post.objects.get(pk=pk)
    if post.user == User.objects.get(username = request.user.get_username()):
        post.delete()
        return redirect('post')
    else:
        return HttpResponse('삭제할 권한이 없습니다.')



def home(request):   #메인 홈
    return render(request, 'blog/wellcome.html')



def join(request):   #회원 가입
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
        else:
            return HttpResponse('아이디나 비밀번호가 틀렸습니다.  다시시도 해주세요')
    else:
        form = JoinForm()
        args = {'form': form}
        return render(request, 'blog/join.html', args)



#로그인/ 로그아웃

login = LoginView.as_view(template_name='registration/login.html')

logout = LogoutView.as_view()
