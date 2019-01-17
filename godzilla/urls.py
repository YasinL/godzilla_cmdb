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
    url(r'^permanager/userlist',views.userlist,name="userlist"),
    url(r'^platformconf/redislist',views.redislist,name="redislist"),
    url(r'^platformconf/cacheconfig',views.redislist,name="redislist"),
    url(r'^platformconf/redisadd',views.redisadd,name="redisadd"),
    url(r'^platformconf/redisedit',views.redisedit,name="redisedit"),
    url(r'^platformconf/redisupdate',views.redisupdate,name="redisupdate"),
    url(r'^platformconf/redishostdel',views.redishostdel,name="redishostdel"),
    url(r'^cachemanager/cache', views.cachelist, name="cachelist"),
    url(r'^cachemanager/redis_get', views.redis_get, name="redis_get"),
    url(r'^cachemanager/redis_del', views.redis_del, name="redis_del"),
    url(r'^cachemanager/matchingdel', views.matchingdel, name="matchingdel"),
    url(r'^cachemanager/graynumber', views.graylist, name="graynumber"),
    url(r'^cachemanager/grayadd', views.grayadd, name="grayadd"),
    url(r'^cachemanager/delphone', views.delphone, name="delphone"),
    url(r'^hostmanager/hostlist', views.hostlist, name="hostlist"),

    url(r'^permanager/useradd',views.useradd,name="useradd"),


    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }),
]


app_name = 'godzilla'