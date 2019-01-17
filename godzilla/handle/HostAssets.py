
import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

from godzilla.models import ansible_host
from godzilla.core.Pager import Pager
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator


@login_decorator
def hostlist(request):
    if request.method == "POST":
        pass
    else:
        host_current_page = request.GET.get('page',1)
        host_page = Pager(host_current_page)
        #把方法改造成属性(2),这样在下面调用方法的时候就不需要加括号了
        results = ansible_host.objects.all().order_by("-hostip")[host_page.start:host_page.end]


        host_all_item = ansible_host.objects.all().count()
        host_pager_str = host_page.page_str(host_all_item,'hostlist/')



        return render(request,'host-list.html',{'result':results,'pager_str':host_pager_str})






def hostadd(request):
    if request.method == "POST":
        host = request.body
        hostinfo = json.loads(host)
        hostname = hostinfo[0]["hostname"]
        hostip = hostinfo[0]["hostip"]
        hostport  = hostinfo[0]["hostport"]
        project_owner  = hostinfo[0]["project_owner"]
        idc_name  = hostinfo[0]["idc_name"]
        try:
            hosthost = ansible_host.objects.filter(host_ip__exact=hostip)
            if len(list(hosthost)) == 0:
                try:
                    hosttable = ansible_host.objects.create(hostip=hostip,hostport=hostport,hostname=hostname,
                                                            project_owner=project_owner,idc_name=idc_name)
                    hosttable.save()

                    hosterror = "缓存添加成功"

                except BaseException as e:
                    logger.error(e)
                    hosterror = "缓存添加失败"
            else:
                hosterror = "缓存地址已存在无需重复添加"

        except BaseException as e:
            logger.error(e)
            hosterror = "数据库查询失败"

        return HttpResponse(hosterror)

    else:
        return  render_to_response('codis-add.html')


def hostdel(request):
    if request.method == "POST":
        pass
    else:
        hostip = request.GET["hostip"]

        ansible_host.objects.filter(hostip=hostip).delete()

        return HttpResponseRedirect('/godzilla/platformconf/hostlist')



def hostupdate(request):
    if request.method == "POST":
        host = request.body
        hostinfo = json.loads(host)
        hostname = hostinfo[0]["hostname"]
        hostip = hostinfo[0]["hostip"]
        hostport = hostinfo[0]["hostport"]
        project_owner = hostinfo[0]["project_owner"]
        idc_name = hostinfo[0]["idc_name"]
        try:
            ansible_host.objects.filter(hostip__exact=hostip).update(hostip=hostip,hostport=hostport,hostname=hostname,
                                                            project_owner=project_owner,idc_name=idc_name)
            hosterror = "缓存信息更新成功"

        except BaseException as e:
            logger.error(e)
            hosterror = "缓存信息更新失败"

        return HttpResponse(hosterror)

    else:
        return  render_to_response('host-list.html')



def hostedit(request):
    hostinfo = []
    if request.method == "POST":
        pass
    else:
        hostip = request.GET["hostip"]
        hosttable = ansible_host.objects.filter(hostip__exact=hostip).values()

        for host in hosttable:
            hostinfo.append(host)

        return  render_to_response('codis-edit.html',{"hostinfo":hostinfo})
