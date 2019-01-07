from django.db import models
from django.conf import settings
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField(upload_to='user_image',blank=True,null=True)

class User(models.Model):
    username = models.CharField(max_length=8)
    email = models.EmailField()
    password = models.CharField(max_length=10)
# Create your models here.
