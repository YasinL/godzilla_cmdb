#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.conf.urls import url
import godzilla.views as views
from django.conf import settings
from django.views import static



urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^index',views.index,name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^alogout', views.alogout, name="alogout"),
    url(r'^welcome',views.welcome,name="welcome"),
    url(r'^permanager/rolemanager',views.rolemanager,name="rolemanager"),
    url(r'^permanager/roleadd',views.roleadd,name="roleadd"),


    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }),
]


app_name = 'godzilla'