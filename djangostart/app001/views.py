from django.shortcuts import render,HttpResponse
from .models import UserInfo
# Create your views here.

def test(req):
    return render(req, 'app001/login.html')


def demo_form(request):
    # print(request.method)

    username = request.GET.get("username")
    password = request.GET.get("password")

    return render(request, 'app001/login.html', {"user":username})

def demo_form2(request):
    userlist = {"cz":"123456"}
    # print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username in userlist and password == userlist.get(username):
            return render(request,'app001/test.html',{"user":username})
    return render(request, 'app001/login.html')

def demo_db(request):
    msg = ""
    # print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            result = UserInfo.objects.get(username=username)
            if result and result.password == password:
                return demo_index(request)
            else:
                msg = "用户名或密码错误"
        except Exception as ex:
            msg = "用户不存在"
    kwgs = {
        "msg":msg
    }
    return render(request, 'app001/login.html', kwgs)


def demo_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        UserInfo.objects.create(username=username,password=password)
    user_list = UserInfo.objects.all()
    return render(request,'app001/register.html')

def demo_index(request):
    user_list = UserInfo.objects.all()
    return render(request,'app001/index.html',{"user_list":user_list})