"""authot:
   data:
"""
from django import forms

from django.contrib.auth.models import User


# 定义一个表单
class ContactForm(forms.Form):
    # 一个属性就是一个表单元素
    # forms.CharField 字段类型
    '''
        label  设置标题
        required  True默认必填项
        min_length  内容最短长度
        initial  初始化的值
        error_messages 设置错误提示信息，后端验证error
    '''
    # widgets 小部件
    subject = forms.CharField(label="主题",
                              min_length=9,
                              # required=True,
                              # initial="Django-Form",
                              error_messages={
                                  "min_length":"主题最少为8字符",
                                  "required":"主题是必填项",
                              })

    content2 = forms.CharField(label="正文2",
                               widget=forms.Textarea(
                                        attrs={
                                            "name":"content2",
                                            "class":"class",
                                            "style":"color:red;font-size:20px",
                                            "cols":20,
                                        }
                                    )


                               )

    sender = forms.EmailField(label="发送人")
    cc_myself = forms.BooleanField(label="抄送")
    # 密码字段
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    # 单radio值为字符串
    gender = forms.fields.ChoiceField(
        choices=((1,"男"),(2,"女"),(3,"保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect(),
    )



# 通过django.forms定义表单

class RegisterForm(forms.Form):
    """注册表单"""
    username = forms.CharField(label="用户名", max_length=30,widget=forms.TextInput(attrs={"size":20,}))
    email = forms.EmailField(label="邮箱", max_length=30,widget=forms.TextInput(attrs={"size":20,}))
    password1 = forms.CharField(label="密码1", max_length=30,widget=forms.PasswordInput(attrs={"size":20,}))
    password2 = forms.CharField(label="密码2", max_length=30,widget=forms.PasswordInput(attrs={"size":20,}))

    def clean(self):
        """
        验证两次输入的密码是否一致 不需要自己返回数据
        """
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        print(password1, password2)
        if password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致")

    def clean_username(self):
        '''验证重复昵称，需要返回字段值'''
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError("该昵称已经被使用请使用其他的昵称")

    def clean_email(self):
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError("该邮箱已经被使用请使用其他的")

class LoginForm(forms.ModelForm):
    """登录表单"""
    username = forms.CharField(label="用户名", max_length=30, widget=forms.TextInput(attrs={"size": 20, }))
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput(attrs={"size": 20, }))

