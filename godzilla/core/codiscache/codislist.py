

import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

from godzilla.models import RedisHost
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator



def cachelist(request):
    redisip = []
    if request.method == "POST":
        pass
    else:
        redistable = RedisHost.objects.all().values()
        for redis in redistable:
            redisip.append(redis)

        return  render_to_response('cache-list.html',{"redisip":redisip})


@login_decorator
def redislist(request):
    redisip = []
    if request.method == "POST":
        pass
    else:
        redistable = RedisHost.objects.all().values()
        for redis in redistable:
            redisip.append(redis)

        return  render_to_response('codis-list.html',{"redisip":redisip})


@login_decorator
def redisadd(request):
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxy_name  = redisinfo[0]["proxy_name"]
        ip  = redisinfo[0]["ip"]
        port  = redisinfo[0]["port"]
        typeid  = redisinfo[0]["typeid"]
        typename  = redisinfo[0]["typename"]
        owner  = redisinfo[0]["owner"]
        principal  = redisinfo[0]["principal"]
        try:
            redishost = RedisHost.objects.filter(redis_ip__exact=ip).filter(redis_port__exact=port)
            if  len(list(redishost)) == 0:
                try:
                    redistable = RedisHost.objects.create(redis_ip=ip,redis_port=port,proxy_name=proxy_name,
                                                         typeid=typeid,typename=typename,project_owner=owner,project_principal=principal)
                    redistable.save()

                    rediserror = "缓存添加成功"

                except BaseException as e:
                    logger.error(e)
                    rediserror = "缓存添加失败"
            else:
                rediserror = "缓存地址已存在无需重复添加"

        except BaseException as e:
            logger.error(e)
            rediserror = "数据库查询失败"

        return HttpResponse(rediserror)

    else:
        return  render_to_response('codis-add.html')

@login_decorator
def redishostdel(request):
    if request.method == "POST":
        pass
    else:
        rowid = request.GET["rowid"]

        RedisHost.objects.filter(id=rowid).delete()

        return HttpResponseRedirect('/godzilla/platformconf/redislist')


@login_decorator
def redisupdate(request):
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        rowid  = redisinfo[0]["rowid"]
        proxy_name  = redisinfo[0]["proxy_name"]
        ip  = redisinfo[0]["ip"]
        port  = redisinfo[0]["port"]
        typeid  = redisinfo[0]["typeid"]
        typename  = redisinfo[0]["typename"]
        owner  = redisinfo[0]["owner"]
        principal  = redisinfo[0]["principal"]

        try:
            RedisHost.objects.filter(id=rowid).update(redis_ip=ip,redis_port=port,proxy_name=proxy_name,
                                                         typeid=typeid,typename=typename,project_owner=owner,project_principal=principal)
            rediserror = "缓存信息更新成功"

        except BaseException as e:
            logger.error(e)
            rediserror = "缓存信息更新失败"

        return HttpResponse(rediserror)

    else:
        return  render_to_response('codis-add.html')


@login_decorator
def redisedit(request):
    redisinfo = []
    if request.method == "POST":
        pass
    else:
        redisip = request.GET["redisip"]
        redistable = RedisHost.objects.filter(redis_ip=redisip).values()

        for redis in redistable:
            redisinfo.append(redis)

        return  render_to_response('codis-edit.html',{"redisinfo":redisinfo})




if __name__ == '__main__':
    redishost = RedisHost.objects.filter(redis_ip="1.1.1.1")
    if len(list(redishost)) == 0:
        print(redishost)
        print("1111")
    else:
        print("222222")
        print(redishost)
