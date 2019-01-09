
# Create your views here.
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from godzilla.handle.login import login
from  godzilla.handle.permission import check_permiss
from  godzilla.handle.role import rolemanager
from  godzilla.handle.role import roleadd
from  godzilla.handle.usermanager import userlist
from  godzilla.handle.usermanager import useradd
from godzilla.handle.rediscacheoperation import redis_get
from godzilla.handle.rediscacheoperation import redis_del
from godzilla.handle.rediscacheoperation import matchingdel
from godzilla.core.codiscache.codislist import redislist
from godzilla.core.codiscache.codislist import redisadd
from godzilla.core.codiscache.codislist import redisedit
from godzilla.core.codiscache.codislist import redisupdate
from godzilla.core.codiscache.codislist import redishostdel
from godzilla.core.codiscache.codislist import cachelist
from godzilla.handle.decorator_login import login_decorator





def index(request):
    username = request.session.get('username')
    permission = check_permiss(username)
    # print(permission)

    if username is not None:
        return render_to_response('index.html', {'username': username,"permission":permission})
    else:
        return render(request,'login.html')

'''登录验证'''
@login_decorator
def welcome(requests):
    if requests.method == "GET":
        return render(requests,"welcome.html")





def alogout(request):
    # logout(request)
    Description = "退出登录"
    username = request.session['username']
    del request.session['username']
    recordvalue = Description + ": 用户 %s 退出系统." % username
    # RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()
    return HttpResponseRedirect('/godzilla/login')


