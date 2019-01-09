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

def redis_get(request):
    redisinfo = []
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxyip  = redisinfo[0]["proxyip"]
        proxyport  = redisinfo[0]["proxyport"]
        key  = redisinfo[0]["key"]
        redis_get = cacheoperation
        redisgetvalue = redis_get(proxyip,proxyport,key).redisoper_get()

        return HttpResponse(redisgetvalue)

    else:
        redisip = request.GET["redisip"]
        redistable = RedisHost.objects.filter(redis_ip=redisip).values()

        for redis in redistable:
            redisinfo.append(redis)

        return render_to_response('redis_get.html',{"redisinfo":redisinfo})



def redis_del(request):
    redisinfo = []
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxyip  = redisinfo[0]["proxyip"]
        proxyport  = redisinfo[0]["proxyport"]
        key  = redisinfo[0]["key"]
        redis_del = cacheoperation
        redisdelvalue = redis_del(proxyip,proxyport,key).redisoper_del()
        return HttpResponse(redisdelvalue)

    else:
        redisip = request.GET["redisip"]
        redistable = RedisHost.objects.filter(redis_ip=redisip).values()

        for redis in redistable:
            redisinfo.append(redis)

        return render_to_response('redis_del.html',{"redisinfo":redisinfo})



def matchingdel(request):
    redisinfo = []
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxyip  = redisinfo[0]["proxyip"]
        proxyport  = redisinfo[0]["proxyport"]
        key  = redisinfo[0]["key"]
        redis_del = cacheoperation
        redisdelvalue = redis_del(proxyip,proxyport,key).TheadPool()

        return HttpResponse(redisdelvalue)

    else:
        redisip = request.GET["redisip"]
        redistable = RedisHost.objects.filter(redis_ip=redisip).values()

        for redis in redistable:
            redisinfo.append(redis)

        return render_to_response('matchingdel.html',{"redisinfo":redisinfo})

