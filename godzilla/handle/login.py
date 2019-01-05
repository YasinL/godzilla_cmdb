from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth import  authenticate,logout
from django.contrib.auth.models import  UserManager
from godzilla.core.Log import logger




def login(request):
    Description = "登录"
    errors = []
    # account = None
    # password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        logger.info(username)

        user = authenticate(username=username,password=password)
        if user is None:
            errors.append('用户名或密码错误')
            return render_to_response('login.html',{'errors':errors})
        else:
            if user.is_active:
                request.session['username'] = username
                recordvalue = Description + ":" + "%s 登录系统" % username
                # RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()
                return HttpResponseRedirect('/godzilla/index')
            else:
                errors.append('用户名或密码错误')
                return render_to_response('login.html',{'error':errors})

        # return render_to_response('login.html')
    else:
        return HttpResponseRedirect('/godzilla/index')


if __name__ == '__main__':
    print("test")
    # print(settings.django_apps_url)