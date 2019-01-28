import os
import json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()

from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from godzilla.models import RedisHost
from godzilla.core.codiscache.cachekeyoperation import cacheoperation
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator
from godzilla.core.RecordLog import RecordLog


def redis_get(request):
    Description = "缓存查询"
    username = request.session.get('username')
    redisinfo = []
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxyip  = redisinfo[0]["proxyip"]
        proxyport  = redisinfo[0]["proxyport"]
        key  = redisinfo[0]["key"]
        redis_get = cacheoperation
        redisgetvalue = redis_get(proxyip,proxyport,key).redisoper_get()

        recordvalue = "查询缓存 %s" % key

        RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()

        return HttpResponse(redisgetvalue)

    else:
        redisip = request.GET["redisip"]
        redistable = RedisHost.objects.filter(redis_ip=redisip).values()

        for redis in redistable:
            redisinfo.append(redis)

        return render_to_response('redis_get.html',{"redisinfo":redisinfo})



def redis_del(request):
    Description = "缓存删除"
    username = request.session.get('username')
    redisinfo = []
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxyip  = redisinfo[0]["proxyip"]
        proxyport  = redisinfo[0]["proxyport"]
        key  = redisinfo[0]["key"]
        redis_del = cacheoperation
        redisdelvalue = redis_del(proxyip,proxyport,key).redisoper_del()

        recordvalue = "删除缓存 %s" % key

        RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()


        return HttpResponse(redisdelvalue)

    else:
        redisip = request.GET["redisip"]
        redistable = RedisHost.objects.filter(redis_ip=redisip).values()

        for redis in redistable:
            redisinfo.append(redis)

        return render_to_response('redis_del.html',{"redisinfo":redisinfo})



def matchingdel(request):
    Description = "缓存模糊删除"
    username = request.session.get('username')
    redisinfo = []
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxyip  = redisinfo[0]["proxyip"]
        proxyport  = redisinfo[0]["proxyport"]
        key  = redisinfo[0]["key"]
        redis_del = cacheoperation
        redisdelvalue = redis_del(proxyip,proxyport,key).TheadPool()

        recordvalue = "模糊删除缓存 %s" % key

        RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()

        return HttpResponse(redisdelvalue)

    else:
        redisip = request.GET["redisip"]
        redistable = RedisHost.objects.filter(redis_ip=redisip).values()

        for redis in redistable:
            redisinfo.append(redis)

        return render_to_response('matchingdel.html',{"redisinfo":redisinfo})

