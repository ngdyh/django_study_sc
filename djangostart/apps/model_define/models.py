from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Category(models.Model):
    """快速上手示例"""
    # 定义字段
    name = models.CharField(max_length=30, verbose_name='分类名称')
    desc = models.CharField(max_length=255, default=None, verbose_name='分类描述')
    index = models.IntegerField(default=999, verbose_name='分类的排序')


    # 设置元数据（设置查询和展示的输出）
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']
        db_table = "category"

    # 类的魔术方法，返回一个友好的显示
    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, verbose_name='名字')
    hobbies = models.CharField(max_length=100,verbose_name='兴趣爱好')
    sex = models.IntegerField(verbose_name="性别")  # 0 => 男生， 1 => 女生
    admission_date = models.DateField(default='2018-01-01')
    # 录入时间
    insert_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 成绩
    english_score = models.FloatField(verbose_name="英语成绩")
    # 学费（跟钱相关的，一定要用这个字段类型）
    schooling = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="学费")
    # 整数位：5位，小数位：2位
    # 只要表单层面验证，不在DB层面验证
    email = models.EmailField(verbose_name="邮箱")
    # 最后登录IP
    last_login_ip = models.GenericIPAddressField(verbose_name="最后登录IP")
    # 当前登录状态
    is_login = models.BooleanField()
    # NullBooleanField默认值是Null
    is_login2 = models.NullBooleanField()
    avator = models.ImageField(upload_to='avator/', default='avator/default.png', verbose_name="用户头像")




    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username