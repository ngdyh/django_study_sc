from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.
def index(request):
    return HttpResponse("route_base_index")

def index2(request):
    return render(request,'route_base/index01.html')

def login(requests, status):
    # 如果用户验证成功，跳转到index页面
    # 否则留在login页面
    if status == 1:
        # 跳转
        # return redirect('/route_base/index/')
        # 反向解析带参数
        print(reverse("route_base:index2"))
        # print(reverse("route_base:zoos3"))
        return redirect(reverse('route_base:index2'))
    else:
        return HttpResponse("这是login页面")

def zoos1(request, zoo_id):
    return HttpResponse(f"{zoo_id}-zoos")

def zoos2(request, id):
    return HttpResponse(f"{id}-zoos")

def zoos3(request, id, type):
    return HttpResponse(f"{id}-zoos-{type}")