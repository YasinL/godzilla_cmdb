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
    url(r'^dashboard/dashboard',views.welcome,name="welcome"),
    url(r'^permanager/rolemanager',views.rolemanager,name="rolemanager"),
    url(r'^permanager/roleadd',views.roleadd,name="roleadd"),
    url(r'^permanager/roledel',views.roledel,name="roledel"),
    url(r'^permanager/userlist',views.userlist,name="userlist"),
    url(r'^permanager/userupdate',views.userupdate,name="userupdate"),
    url(r'^permanager/useradd', views.useradd, name="useradd"),
    url(r'^permanager/userdel', views.userdel, name="userdel"),
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
    url(r'^cachemanager/redisphonecheckstatus', views.redisphonecheckstatus, name="redisphonecheckstatus"),
    url(r'^hostmanager/hostlist', views.hostlist, name="hostlist"),
    url(r'^hostmanager/hostadd', views.hostadd, name="hostadd"),
    url(r'^hostmanager/hostdel', views.hostdel, name="hostdel"),
    url(r'^hostmanager/hostedit', views.hostedit, name="hostedit"),
    url(r'^hostmanager/hostupdate', views.hostupdate, name="hostupdate"),

    url(r'^platformconf/tenginehost$',views.tenginehostlist,name="tenginehostlist"),
    url(r'^platformconf/tenginehostadd',views.tenginehostadd,name="tenginehostadd"),
    url(r'^platformconf/tenginehostdel',views.tenginehostdel,name="tenginehostdel"),
    url(r'^platformconf/tenginehostupdate',views.tenginehostupdate,name="tenginehostupdate"),
    url(r'^platformconf/tenginehostedit',views.tenginehostedit,name="tenginehostedit"),


    url(r'^platformconf/tenginehostedit',views.tenginehostedit,name="tenginehostedit"),
    url(r'^recordlist/recordlist',views.recordlist,name="recordlist"),



    url(r'^platformconf/golabaltool',views.golabaltoolconf,name="golabaltoolconf"),



    url(r'^platformconf/compile_config',views.compile_config,name="compile_config"),
    url(r'^platformconf/compile_config_update',views.compile_config_update,name="compile_config_update"),
    url(r'^platformconf/compile_config_del',views.compile_config_del,name="compile_config_del"),





    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }),
]


app_name = 'godzilla'