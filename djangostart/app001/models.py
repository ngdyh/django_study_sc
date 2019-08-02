from django.db import models

# Create your models here.

# 定义一个表
# class 定义的一个类就是一个表
class UserInfo(models.Model):
    username = models.CharField(max_length=18)
    # 一个属性就是一个字段
    email = models.EmailField()
    # 6-18
    password = models.CharField(max_length=128)

    def __str__(self):  # 这里也可以用__repr__
        return self.username