"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from app001 import views
from django.views.static import serve
from . import settings
import re



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.test),
    url(r'^demo/$', views.demo_form,name="demo"),
    url(r'^demo2/$', views.demo_form2),
    url(r'^demo_login/$', views.demo_db),
    url(r'^demo_register/$', views.demo_register),
    url(r'^index/$', views.demo_index),

    url('^route_base/', include('apps.route_base.urls', namespace='route_base')),
    url('^route_resolve/', include('apps.route_resolve.urls', namespace='route_resolve')),
    url('^django_templates/', include('apps.django_templates.urls', namespace='django_templates')),
    url(r'^forms_base/', include('apps.forms_base.urls', namespace='forms_base')),
    url(r'^forms_auth/', include('apps.forms_auth.urls', namespace='forms_auth')),
    url(r'^django_view/', include('apps.django_view.urls', namespace='django_view')),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, {"document_root": settings.STATIC_ROOT}),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve, {"document_root": settings.MEDIA_ROOT}),

]


handler404 = views.my404
handler500 = views.my500
