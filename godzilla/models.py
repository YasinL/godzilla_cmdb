from django.db import models
from  django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils import  timezone
from django.utils.timezone import datetime

# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
# django.setup()




class users(AbstractUser):
    roleid = models.CharField(max_length=50, verbose_name='角色id', default='')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class ansible_host(models.Model):
    hostip =  models.GenericIPAddressField()
    ansible_groupid = models.CharField(max_length=200, null=True)

class ansible_group(models.Model):
    hostgroup = models.CharField(max_length=200,null=True)
    ansible_groupid = models.CharField(max_length=200, null=True)


class memuid(models.Model):
    submemuname = models.CharField(max_length=50,null=True)
    submemuurl = models.CharField(max_length=50,null=True)
    memunameid = models.CharField(max_length=50,null=True)

class memulist(models.Model):
    permission_url = models.CharField(max_length=50,null=True)
    memuname = models.CharField(max_length=10,null=True)
    memunameid = models.CharField(max_length=10,null=True)
    permission_id = models.CharField(max_length=50,null=True)


class role(models.Model):
    roleid = models.CharField(max_length=10,null=True)
    Rolename = models.CharField(max_length=50,null=True)


class permission(models.Model):
    permission_id = models.CharField(max_length=10,null=True)
    roleid = models.CharField(max_length=10,null=True)


class RedisHost(models.Model):
    redis_ip = models.GenericIPAddressField()
    redis_port = models.CharField(max_length=20,null=False)
    redis_pass = models.CharField(max_length=50,null=True)
    project_owner =  models.CharField(max_length=50,null=True)
    project_principal = models.CharField(max_length=20,null=True)
    typename = models.CharField(max_length=20,null=True)
    typeid = models.CharField(max_length=1,null=True)


class grayphone(models.Model):
    phone = models.CharField(max_length=11)
    expirytime  = models.CharField(max_length=30,null=True)
    phoneencrypt = models.CharField(max_length=150,null=True)
    online = models.CharField(max_length=10)
    createuser = models.CharField(max_length=30)
    createtime = models.CharField(max_length=30,null=True)



class RecordLogTable(models.Model):
    username = models.CharField(max_length=100)
    recordclass = models.CharField(max_length=150)
    recordvalue = models.TextField(max_length=10000)
    logtime = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))