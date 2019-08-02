from django.shortcuts import render

# Create your views here.

def index(request):
    kwgs = {
        "Today_recommend":[
            {"name":"奶茶","msg":"好喝"},
            {"name":"面包","msg":"好吃"},
            {"name":"海鲜","msg":"健康"},
            {"name":"爆米花","msg":"点心"},
        ]
    }
    return render(request, 'django_templates/index.html',kwgs)