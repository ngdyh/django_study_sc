from django.shortcuts import render, HttpResponse ,Http404
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView


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



class MyTemplateView(TemplateView):
    template_name = 'test.html'

class IndexView(ListView):
    template_name = "test.html"
    context_object_name = "userlist"
    model = UserInfo
    queryset = UserInfo.objects.all()


class MyDetailView(DetailView):
    model = UserInfo
    template_name = "test.html"
    # 查询的关键字 --> pk --> 默认主键id
    pk_url_kwarg = "id"
    # 默认名:object
    # context_object_name = ""

    def get_object(self, queryset=None):
        user = super().get_object()
        # user = self.get_object()
        user.abc = "hello"
        return user