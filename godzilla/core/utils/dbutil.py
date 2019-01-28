

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







def table_row_add(request):
    if request.method == "POST":
        host = request.body
        hostinfo = json.loads(host)
        hostname = hostinfo[0]["hostname"]
        hostip = hostinfo[0]["hostip"]
        hostport  = hostinfo[0]["hostport"]
        project_owner  = hostinfo[0]["project_owner"]
        idc_name  = hostinfo[0]["idc_name"]
        try:
            hosthost = ansible_host.objects.filter(hostip__exact=hostip).values()
            print(len(list(hosthost)))
            if len(list(hosthost)) == 0:
                try:
                    hosttable = ansible_host.objects.create(hostip=hostip,hostport=hostport,hostname=hostname,
                                                            project_owner=project_owner,idc_name=idc_name)
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
        return  render_to_response('host-add.html')



