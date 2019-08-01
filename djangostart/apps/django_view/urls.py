"""authot:
   data:
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^zoos/$', views.zoos,name='zoos'),


]