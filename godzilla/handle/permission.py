
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


def check_permiss(username):
    memuidlist = []
    roleid = users.objects.filter(username=username).values('roleid')
    permissiontable = permission.objects.filter(roleid=(roleid)).values('permission_id')

    for permissionid  in permissiontable:
        fatmemu = memulist.objects.filter(permission_id=permissionid["permission_id"]).values()
        for memu in fatmemu:
            submemuid = memuid.objects.filter(memunameid=memu["memunameid"]).values('submemuname','memunameid','submemuurl').annotate()
            memu["submemuname"] = list(submemuid)
            memuidlist.append(memu)

    return memuidlist

if __name__ == '__main__':
    print(check_permiss('admin'))







