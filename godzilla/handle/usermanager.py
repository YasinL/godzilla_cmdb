import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()

from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth import  authenticate,logout
from godzilla.models import users
from django.contrib.auth.models import User
from godzilla.models import role
from godzilla.models import role
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator



'''登录验证
用户添加列表
'''
@login_decorator
def userlist(request):
    userlist = []
    if request.method == "POST":
        pass

    else:
        usertable = users.objects.all().values()
        for user in usertable:
            userlist.append(user)
        return render_to_response('admin-list.html', {'userlist': userlist})


'''登录验证
用户添加  （ajax 请求）
'''
@login_decorator
def useradd(request):
    roleid = []
    if request.method == "POST":
        userbody = request.body
        userinfo = json.loads(userbody)
        username  = userinfo[0]["user"]
        mobile  = userinfo[0]["mobile"]
        email  = userinfo[0]["email"]
        passwd  = userinfo[0]["pass"]
        roleid  = userinfo[0]["roleid"]
        try:
            usertable = users.objects.create_user(username=username, mobile=mobile, email=email, password=passwd,roleid=roleid)
            usertable.save()

            usererror = "用户添加成功"
        except BaseException as e:
            logger.error(e)
            usererror = "用户添加失败"

        return  HttpResponse(usererror)



    else:

        roletable = role.objects.all().values()
        for roles in roletable:
            roleid.append(roles)
        return render_to_response('admin-add.html', {'roleid': roleid})
