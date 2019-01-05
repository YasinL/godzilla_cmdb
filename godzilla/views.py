
# Create your views here.
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from godzilla.handle.login import login
from  godzilla.handle.permission import check_permiss
from  godzilla.handle.role import rolemanager
from  godzilla.handle.role import roleadd






def index(request):
    username = request.session.get('username')
    permission = check_permiss(username)
    print(permission)

    if username is not None:
        return render_to_response('index.html', {'username': username,"permission":permission})
    else:
        return render(request,'login.html')



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


