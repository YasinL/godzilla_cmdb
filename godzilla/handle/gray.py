import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
import hashlib
from godzilla.core.utils.redisutils import RedisConn
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from godzilla.models import grayphone
from godzilla.models import tenginehost
from godzilla.core.Log import logger
from godzilla.core.RecordLog import RecordLog
import datetime
import time
import json










def graynumber():
    pass


def tenginehosts():
    hostlist = []
    tenginehosttable = tenginehost.objects.all().values("host","hostredisport")
    for grayhost in  tenginehosttable:
        hostlist.append(grayhost)

    return hostlist




class Gray():
    def __init__(self, grayredisip, grayredisport, phone):
        self.__conn = RedisConn(grayredisip, grayredisport)
        self.phone = phone

    def graymd5value(self):
        graymd5 = hashlib.md5()
        strmd5 = "ecmc" + str(self.phone)
        graymd5.update(strmd5.encode("utf8"))
        return graymd5.hexdigest().upper()

    def grayaddphone(self, username, expirytime, createtime):

        try:
            addphone = grayphone.objects.create(phone=self.phone, phoneencrypt=self.graymd5value(),
                                                online=self.phoneonline(), expirytime=expirytime, createuser=username,
                                                createtime=createtime)
            addphone.save()
            addstatus = "添加手机号码 %s 成功" % self.phone
        except BaseException as e:
            logger.error(e)
            addstatus = "添加手机号码 %s 失败" % self.phone

        return addstatus

    def grayaddredisphone(self, duration):
        try:
            keyvalue = self.graymd5value()
            self.__conn.set(keyvalue, keyvalue, duration)

            addredisstatus = "添加手机号码 %s 成功" % self.phone
        except BaseException as e:
            logger.error(e)
            addredisstatus = "添加手机号码 %s 失败" % self.phone

        return addredisstatus

    def graydelredisphone(self):
        try:
            self.__conn.delete(self.graymd5value())
            delredisphonestatus = 0
        except BaseException as e:
            logger.error(e)
            delredisphonestatus = 1

        return delredisphonestatus

    def graydelphone(self):
        try:
            grayphone.objects.filter(phone__exact=self.phone).delete()
            delstatus = "删除手机号码 %s 成功" % self.phone
        except BaseException as e:
            logger.error(e)
            delstatus = "删除手机号码 %s 失败" % self.phone
        return delstatus

    @classmethod
    def graylistphone(self):
        phonelist = []
        listphone = grayphone.objects.values()
        for phone in listphone:
            # django mysql 获取datatime类型字段转化
            # phone["CreateTime"] = phone.get("CreateTime").strftime('%Y-%m-%d %H:%M:%S')
            phonelist.append(phone)

        return phonelist
        # return self.conn.keys()

    def phoneonline(self):
        onlinestatus = self.__conn.exists(self.graymd5value())
        if onlinestatus is True:
            onlinestatus = "YES"
        else:
            onlinestatus = "NO"
        return onlinestatus

    def checkstatus(self):
        status = self.__conn.exists(self.graymd5value())
        return status



def graylist(request):
    if request.method == "POST":
        pass
    else:
        graylist = Gray.graylistphone()
        return render(request, "gray-list.html", {'graylist': graylist})





def grayadd(request):
    Description = "添加灰度白名单"
    if request.method == "POST":
        grayrequest = request.body
        grayinfo = json.loads(grayrequest)
        grayphone  = grayinfo[0]["phone"]
        duration  = grayinfo[0]["duration"]
        username = request.session.get('username')
        dtime = datetime.datetime.now()
        un_time = time.mktime(dtime.timetuple())
        expirytime = int(un_time) + int(duration)
        expirytime = datetime.datetime.fromtimestamp(expirytime)
        createtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        for gray in tenginehosts():
            Gray(gray.get("host"), gray.get("hostredisport"), grayphone).grayaddredisphone(duration=duration)

        addphonestatus = Gray(tenginehosts()[0]["host"], tenginehosts()[0]["hostredisport"], grayphone).grayaddphone(username=username, expirytime=expirytime,createtime=createtime)

        recordvalue = "添加手机号 %s 到灰度白名单"  % grayphone
        RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()



        return HttpResponse(addphonestatus)

    else:
        return render(request, "gray-add.html")


def delphone(request):
    Description = "删除灰度白名单"
    if request.method == "GET":
        grayphone = request.GET.get("phone")
        username = request.session.get("username")
        for gray in tenginehosts():
            Gray(gray.get("host"), gray.get("hostredisport"), grayphone).graydelredisphone()


        graydelphone = Gray(tenginehosts()[0]["host"], tenginehosts()[0]["hostredisport"], grayphone).graydelphone()


        recordvalue = "从白名单中删除手机号"  % grayphone
        RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()


        return HttpResponse(graydelphone)


def redisphonecheckstatus(request):
    Description = "白名单有效检测"
    stat = []
    if request.method == "POST":
        jsondata = json.loads(request.body)
        print(jsondata)
        username = request.session.get("username")

        for data in jsondata:
            phone = data.get("phone")
            status = Gray(tenginehosts()[0]["host"], tenginehosts()[0]["hostredisport"], phone).checkstatus()
            if status is True:
                code = 0
            else:
                Gray(tenginehosts()[0]["host"], tenginehosts()[0]["hostredisport"], phone).graydelphone()
                code = 1

                recordvalue = "删除手机号码： " + phone

                RecordLog(username=username, recordclass=Description, recordvalue=recordvalue).saveecord()


        return HttpResponseRedirect('/godzilla/cachemanager/grayadd')
        # return  HttpResponse.status_code(200)


if __name__ == '__main__':
    test = tenginehosts()
    print(test[0]["host"])

    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__())

    # print(Gray(grayredisip="118.89.18.234",grayredisport="6379",phone=15269136818).graymd5value())
    # Gray("12569136818").conn(grayredisip="118.89.18.234",grayredisport="6379").set("123","33333")
    # 将python的datetime转换为unix时间戳
    # dtime = datetime.datetime.now()
    # un_time = time.mktime(dtime.timetuple())
    # print(un_time)
    # print(Gray(grayredisip,grayredisport,"15269136818").grayaddphone("admin"))
    # print(Gray.graylistphone())
    # # print(GetConf(section="grayredis",key="port"))
    # graymd5 = hashlib.md5()
    # graymd5.update(b'xwtec123')
    # print(graymd5.hexdigest())

