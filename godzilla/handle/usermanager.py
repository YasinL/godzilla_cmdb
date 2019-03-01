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





class UserOper():
    def __init__(self,username,mobile,email,passwd,roleid):
        self.username = username
        self.mobile = mobile
        self.email = email
        self.passwd = passwd
        self.roleid = roleid


    def useradd(self):
        try:
            usertable = users.objects.create_user(
                username=self.username,
                mobile=self.mobile,
                email=self.email,
                password=self.passwd,
                roleid=self.roleid
            )

            usertable.save()

            useradderror = "用户添加成功"
        except BaseException as e:
            logger.error(e)
            useradderror = "用户添加失败"

        return useradderror


    def userupdate(self):
        try:
            usertable = users.objects.filter(username=self.username).update(
                mobile=self.mobile,
                email=self.email,
                password=self.passwd,
                roleid=self.roleid
            )
            usertable.save()

            usererror = "用户更新成功"
        except BaseException as e:
            logger.error(e)
            usererror = "用户更新失败"

        return  HttpResponse(usererror)


    @classmethod
    def userdel(self,username):
        try:
            users.objects.filter(username=username).delete()
            userdelerror = "用户删除成功"
        except BaseException as e:
            logger.error(e)
            userdelerror = "用户删除失败"

        return  userdelerror




'''登录验证
用户添加列表
'''
@login_decorator
def userlist(request):
    userlist = []
    if request.method == "POST":
        pass

    else:
        print(request.path)
        print(request.path.split("/")[2])
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


        useradd  = UserOper(username=username, mobile=mobile, email=email,passwd=passwd,roleid=roleid).useradd()

        return  HttpResponse(useradd)



    else:

        roletable = role.objects.all().values()
        for roles in roletable:
            roleid.append(roles)
        return render_to_response('admin-add.html', {'roleid': roleid})





'''登录验证
用户更新  （ajax 请求）
'''
@login_decorator
def userupdate(request):
    roleid = []
    if request.method == "POST":
        userbody = request.body
        userinfo = json.loads(userbody)
        username  = userinfo[0]["user"]
        mobile  = userinfo[0]["mobile"]
        email  = userinfo[0]["email"]
        passwd  = userinfo[0]["pass"]
        roleid  = userinfo[0]["roleid"]

        userupdate  = UserOper(username=username, mobile=mobile, email=email,passwd=passwd,roleid=roleid).userupdate()


        return  HttpResponse(userupdate)



    else:
        userid = request.GET["userid"]
        userinfolist = []
        roletable = role.objects.all().values()
        for roles in roletable:
            roleid.append(roles)

        userinfo = users.objects.filter(id__exact=userid).values()
        for user in userinfo:
            userinfolist.append(user)


        return render_to_response('admin-edit.html', {'roleid':roleid,"userinfo":userinfolist})




'''登录验证
用户删除  （ajax 请求）
'''
@login_decorator
def userdel(request):
    roleid = []
    if request.method == "POST":
        pass


    else:
        username = request.GET["username"]
        userdel = UserOper.userdel(username)

        return HttpResponse(userdel)