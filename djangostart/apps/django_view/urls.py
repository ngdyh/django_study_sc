"""authot:
   data:
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^zoos/$', views.zoos,name='zoos'),
    url(r'^templateview/$', views.MyTemplateView.as_view(), name='templateview'),
    url(r'^indexview/$', views.IndexView.as_view(), name='indexview'),
    url(r'^detailview/(?P<id>\d)/$', views.MyDetailView.as_view(), name='detailview'),
]