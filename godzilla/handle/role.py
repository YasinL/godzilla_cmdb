import os
import json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()

from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth import  authenticate,logout
from godzilla.models import users
from godzilla.models import role
from godzilla.models import permission
from godzilla.models import memuid
from godzilla.models import memulist
from godzilla.handle.permission import addrole
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator

'''登录验证
角色列表
'''
@login_decorator
def rolemanager(request):

    if request.method == "POST":
        pass
    else:

        return render(request,'admin-role.html')


'''登录验证
角色添加
'''
@login_decorator
def roleadd(request):
    if request.method == "POST":
        rolebody = request.body
        rolejson = json.loads(rolebody)
        rolename = rolejson[0]["rolename"]
        permissionid = rolejson[0]["permissionid"]
        addroleerror = addrole(permissionudnum=permissionid,rolename=rolename)
        return  HttpResponse(addroleerror)
    else:
        rolememulist = []
        rolememu = memulist.objects.all().values()
        for memu in rolememu:
            rolememulist.append(memu)
        return render_to_response('role-add.html', {'memu': rolememulist})