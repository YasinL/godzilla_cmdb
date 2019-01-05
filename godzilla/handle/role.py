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
from godzilla.core.Log import logger



def rolemanager(request):

    if request.method == "POST":
        pass
    else:

        return render(request,'admin-role.html')


def roleadd(request):
    if request.method == "POST":
        pass
    else:
        rolememulist = []
        rolememu = memulist.objects.all().values()
        for memu in rolememu:
            rolememulist.append(memu)
        return render_to_response('role-add.html', {'memu': rolememulist})