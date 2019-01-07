from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('blog/', views.post, name='post'),
    path('test/new/',views.test,name='test'),
    path('blog/index/<int:pk>/',views.index, name="index"),
    path('blog/index/<int:pk>/del/',views.delete,name="delete"),
    path('join/',views.join, name='join'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('blog/edit/<int:pk>/',views.edit, name='edit')
]