

import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator
from godzilla.models import compile_conf
from godzilla.core.utils.randomnum import randomnumutil

# 编译环境配置  maven and jdk path
class Config():
    def __init__(self,var,varpath):
        self.var = var
        self.varpath = varpath
        self.randnum = randomnumutil()



    def varadd(self):
        try:
            confadd = compile_conf.objects.create(varname=self.var,varpath=self.varpath,varnameid=self.randnum)
            confadd.save()
            conferror = ("保存变量 %s 成功" %self.var)

        except BaseException as e:
            logger.error("编译环境配置失败，变量名称 %s 保存不成功" %self.var)
            conferror = ("保存变量 %s 失败" % self.var)

        return  conferror


    def vardel(self,varnameid):
        try:
            compile_conf.objects.filter(varnameid=varnameid).delete()
            confdelerror = ("删除变量 %s 成功" % self.var)

        except BaseException as e:
            logger.error("变量名称 %s 删除不成功" % self.var)
            confdelerror = ("删除变量 %s 失败" % self.var)

        return confdelerror

    def varupdate(self,varnameid):
        try:
            compile_conf.objects.filter(varnameid=varnameid).update(varname=self.var,varpath=self.varpath)
            confuperror = ("更新变量 %s 成功" % self.var)

        except BaseException as e:
            logger.error("变量名称 %s 更新不成功" % self.var)
            confuperror = ("更新变量 %s 失败" % self.var)

        return confuperror




