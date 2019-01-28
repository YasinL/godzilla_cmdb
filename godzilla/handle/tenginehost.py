
import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

from godzilla.models import ansible_host
from godzilla.models import tenginehost
from godzilla.core.Pager import Pager
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator


@login_decorator
def tenginehostlist(request):
    if request.method == "POST":
        pass
    else:
        host_current_page = request.GET.get('page',1)
        host_page = Pager(host_current_page)
        #把方法改造成属性(2),这样在下面调用方法的时候就不需要加括号了
        results = tenginehost.objects.all().order_by("-host")[host_page.start:host_page.end]


        host_all_item = tenginehost.objects.all().count()
        host_pager_str = host_page.page_str(host_all_item,'tenginehostlist/')



        return render(request,'tengine_list.html',{'result':results,'pager_str':host_pager_str})






def tenginehostadd(request):
    if request.method == "POST":
        host = request.body
        hostinfo = json.loads(host)
        hostip = hostinfo[0]["hostip"]
        hostport = hostinfo[0]["hostport"]

        try:
            hosthost = tenginehost.objects.filter(host__exact=hostip).values()
            print(len(list(hosthost)))
            if len(list(hosthost)) == 0:
                try:
                    hosttable = tenginehost.objects.create(host=hostip,hostredisport=hostport)
                    hosttable.save()

                    hosterror = "主机添加成功"

                except BaseException as e:
                    logger.error(e)
                    hosterror = "主机添加失败"
            else:
                hosterror = "主机地址已存在无需重复添加"

        except BaseException as e:
            logger.error(e)
            hosterror = "数据库查询失败"

        return HttpResponse(hosterror)

    else:
        return  render_to_response('tengine_add.html')


def tenginehostdel(request):
    if request.method == "POST":
        pass
    else:
        hostip = request.GET["hostip"]
        try:
            tenginehost.objects.filter(host=hostip).delete()
            hostdelerror = "删除主机成功"
        except BaseException as e:
            logger.error(e)
            hostdelerror = "删除主机失败"


        return  HttpResponse(hostdelerror)



def tenginehostupdate(request):
    if request.method == "POST":
        host = request.body
        hostinfo = json.loads(host)
        hostip = hostinfo[0]["hostip"]
        hostport = hostinfo[0]["hostport"]
        try:
            tenginehost.objects.filter(host__exact=hostip).update(host=hostip,hostredisport=hostport)
            hosterror = "主机信息更新成功"

        except BaseException as e:
            logger.error(e)
            hosterror = "主机信息更新失败"

        return HttpResponse(hosterror)

    else:
        hostinfo = []
        hostip = request.GET["hostip"]
        hosttable = tenginehost.objects.filter(host__exact=hostip).values()

        for host in hosttable:
            hostinfo.append(host)

        return render_to_response('tengine_edit.html', {"hostinfo": hostinfo})



def tenginehostedit(request):
    hostinfo = []
    if request.method == "POST":
        pass
    else:
        hostip = request.GET["hostip"]
        hosttable = tenginehost.objects.filter(host__exact=hostip).values()

        for host in hosttable:
            hostinfo.append(host)

        return  render_to_response('tengine_edit.html',{"hostinfo":hostinfo})
