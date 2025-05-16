from django.db import models

#注册用户表
class User(models.Model):
    user=models.CharField(max_length=30)#用户名
    password=models.IntegerField(max_length=100)#密码

# Create your models here.
