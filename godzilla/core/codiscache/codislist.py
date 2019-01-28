

import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

from godzilla.models import RedisHost
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator
from godzilla.core.RecordLog import RecordLog


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
    Description = "添加缓存地址"
    if request.method == "POST":
        redis = request.body
        redisinfo = json.loads(redis)
        proxy_name  = redisinfo[0]["proxy_name"]
        proxy_ip  = redisinfo[0]["proxy_ip"]
        proxy_port  = redisinfo[0]["proxy_port"]
        admin_ip  = redisinfo[0]["admin_ip"]
        admin_port  = redisinfo[0]["admin_port"]
        typeid  = redisinfo[0]["typeid"]
        typename  = redisinfo[0]["typename"]
        owner  = redisinfo[0]["owner"]
        principal  = redisinfo[0]["principal"]
        username = request.session.get('username')

        try:
            redishost = RedisHost.objects.filter(redis_ip__exact=proxy_ip).filter(redis_port__exact=proxy_port)
            if  len(list(redishost)) == 0:
                try:
                    redistable = RedisHost.objects.create(redis_ip=proxy_ip,redis_port=proxy_port,proxy_name=proxy_name,admin_addr=admin_ip,admin_port=admin_port,
                                                         typeid=typeid,typename=typename,project_owner=owner,project_principal=principal)
                    redistable.save()

                    rediserror = "添加缓存 %s:%s 成功" % (proxy_ip,proxy_port)


                    RecordLog(username=username, recordclass=Description, recordvalue=rediserror).saveecord()

                except BaseException as e:
                    logger.error(e)
                    rediserror = "添加缓存 %s:%s 失败" % (proxy_ip, proxy_port)

                    RecordLog(username=username, recordclass=Description, recordvalue=rediserror).saveecord()

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
    username = request.session.get('username')
    Description = "删除缓存地址"
    if request.method == "POST":
        pass
    else:
        redis_ip = request.GET["redis_ip"]
        redis_port = request.GET["redis_port"]

        RedisHost.objects.filter(redis_ip__exact=redis_ip).filter(redis_port__exact=redis_port).delete()

        recordvalue = "删除缓存地址 %s:%s 成功 " % (redis_ip,redis_port)
        RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()

        return HttpResponseRedirect('/godzilla/platformconf/redislist')


@login_decorator
def redisupdate(request):

    Description = "更新缓存地址"
    username = request.session.get('username')
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


            RecordLog(username=username, recordclass=Description, recordvalue=rediserror).saveecord()

        except BaseException as e:
            logger.error(e)
            rediserror = "缓存信息更新失败"
            RecordLog(username=username, recordclass=Description, recordvalue=rediserror).saveecord()

        return HttpResponse(rediserror)

    else:
        redisinfo = []
        rowid = request.GET["rowid"]
        redistable = RedisHost.objects.filter(id=rowid).values()

        for redis in redistable:
            redisinfo.append(redis)

        return  render_to_response('codis-edit.html',{"redisinfo":redisinfo})


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
