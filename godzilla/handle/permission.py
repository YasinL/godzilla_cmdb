
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
import random
import string


def check_permiss(username):
    memuidlist = []
    roleid = users.objects.filter(username__exact=username).values('roleid')
    permissiontable = permission.objects.filter(roleid__exact=roleid).values('permission_id')

    for permissionid  in permissiontable:
        fatmemu = memulist.objects.filter(permission_id=permissionid["permission_id"]).values()
        for memu in fatmemu:
            submemuid = memuid.objects.filter(memunameid=memu["memunameid"]).values('submemuname','memunameid','submemuurl').annotate()
            memu["submemuname"] = list(submemuid)
            memuidlist.append(memu)

    return memuidlist


class RoleOper():
    def __init__(self,permissionudnum,rolename):
        self.permissionudnum =permissionudnum
        self.rolename = rolename

    def addrole(self):
        roleidnum = "1" + "".join(map(lambda x:random.choice(string.digits), range(7)))
        try:
            roletable = role.objects.create(roleid=roleidnum, Rolename=self.rolename)
            roletable.save()

            for permissionid in self.permissionudnum:
                permissiontable = permission.objects.create(permission_id=permissionid,roleid=roleidnum)
                permissiontable.save()

            addroleerror = "角色添加成功"


        except BaseException as e:
            logger.error(e)
            addroleerror = "角色添加失败"

        return addroleerror



    def update(self):
        try:
            role.objects.filter(roleid__exact=self.permissionudnum).update(Rolename=self.rolename)

            addroleerror = "角色更新成功"


        except BaseException as e:
            logger.error(e)
            addroleerror = "角色更新失败"

        return addroleerror

    @classmethod
    def roledel(self,permissionid):
        try:
            role.objects.filter(roleid__exact=permissionid).delete()
            permission.objects.filter(roleid__exact=permissionid).delete()

            addroleerror = "角色删除成功"


        except BaseException as e:
            logger.error(e)
            addroleerror = "角色删除失败"

        return addroleerror



if __name__ == '__main__':
    # print(check_permiss('admin'))
    roleid = "1" +  "".join(map(lambda x:random.choice(string.digits), range(7)))
    print(roleid)







