
import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from godzilla.core.compile.config import Config
from godzilla.models import compile_conf



def compile_config(request):
    if request.method == "POST":
        pass

    else:
        varinfo = []
        list = compile_conf.objects.values().all()
        for var in list:
            varinfo.append(var)


        return render_to_response('compile_config.html',{"varinfo":varinfo})



def compile_config_add(request):
    if request.method == "POST":
        pass

    else:
        varinfo = []
        list = compile_conf.objects.values().all()
        for var in list:
            varinfo.append(var)


        return render_to_response('compile_config.html',{"varinfo":varinfo})


def compile_config_del(request):
    if request.method == "POST":
        pass

    else:
        varinfo = []
        list = compile_conf.objects.values().all()
        for var in list:
            varinfo.append(var)


        return render_to_response('compile_config.html',{"varinfo":varinfo})






def compile_config_update(request):
    if request.method == "POST":

        pass

    else:
        varinfo = []
        varnameid = request.GET["varnameid"]
        list = compile_conf.objects.filter(varnameid__exact=varnameid).values()
        for var in list:
            varinfo.append(var)


        return render_to_response('compile_config.html',{"varinfo":varinfo})

