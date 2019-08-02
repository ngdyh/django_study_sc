from django.shortcuts import render, HttpResponse ,Http404
from django.http import JsonResponse

# Create your views here.

def view_test(request):
    html = '<h1>i am demo01</h1>'
    print(html)
    return HttpResponse(html, status=404, charset="utf-8")


def zoos(request, id):
    # get_object_or_404 --> 从model中获取数据, 如果没有获取到, 就raise一个Http404
    id = int(id)
    if id > 100:
        raise Http404('not exist')
    return HttpResponse('这是第{id}个动物园信息')

from app001.models import UserInfo