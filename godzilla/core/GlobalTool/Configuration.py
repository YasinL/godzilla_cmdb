
import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from godzilla.core.compile.config import Config
from godzilla.models import globaltool



def golabaltoolconf(request):
    if request.method == "POST":
        globaltool = request.body
        globalinfo = json.loads(globaltool)
        maven = globalinfo[0]["maven"]
        jdk = globalinfo[0]["jdk"]
        git = globalinfo[0]["git"]
        mavenname = globalinfo[0]["mavenname"]
        mavenpath = globalinfo[0]["mavenpath"]
        jdkname = globalinfo[0]["jdkname"]
        jdkpath = globalinfo[0]["jdkpath"]
        gitname = globalinfo[0]["gitname"]
        gitpath = globalinfo[0]["gitpath"]



    else:

        return render_to_response('globaltool.html')
