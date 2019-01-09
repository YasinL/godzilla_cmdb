import os
import  json
import django
import  requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

from godzilla.models import RedisHost
from godzilla.core.utils.redisutils import RedisConn
from godzilla.core.Log import logger
from multiprocessing import Process,Manager,Lock,Pool
from godzilla.handle.decorator_login import login_decorator

class pullsubnode():
    def __init__(self,redisip,redisport):
        self.redisip = redisip
        self.redisport = redisport


    def selectadmminaddr(self):
        try:
            redistable = RedisHost.objects.filter(redis_ip__exact=self.redisip,redis_port__exact=self.redisport).values(
                'admin_addr','admin_port')
            redistablevalue  = list(redistable)

            admin_addr_link = "http://%s:%s/proxy/slots" % (redistablevalue[0]["admin_addr"],redistablevalue[0]["admin_port"])

        except BaseException as e:
            logger.error(e)
            admin_addr_link = False

        return  admin_addr_link

    def subnode(self):
        if self.selectadmminaddr():
            response = requests.get(self.selectadmminaddr()).content
            jsonresponse = json.loads(response)
            slotslist = []
            for subnode in jsonresponse:
                slotslist.append(subnode["backend_addr"])
            subnodelist = list(set(slotslist))

            return subnodelist
        else:
            subnodelist = False

            return subnodelist



class cacheoperation():

    def __init__(self,proxyip,proxyport,key):
        self.proxyip =proxyip
        self.proxyport = proxyport
        self.key = key


    def  redisoper_get(self):
        redisconn = RedisConn(self.proxyip,self.proxyport)
        keyvalue = redisconn.exists(self.key)
        if keyvalue is True:
            try:
                keyvalue = str(redisconn.get(self.key))
                if keyvalue == None:
                    keyvalue = "KEY 不存在"
            except BaseException as e:
                logger.error("获取key %s ,ERROR:%s" % (self.key,e))
                keyvalue = "ERROR:获取key值出错"

            return keyvalue
        else:
            keyvalue = "ERROR:key 不存在"
        return  keyvalue


    def redisoper_del(self):
        redisconn = RedisConn(self.proxyip, self.proxyport)
        keyvalue = redisconn.exists(self.key)
        if keyvalue is True:
            try:
                keyvalue = str(redisconn.delete(self.key))
                if keyvalue == "None":
                    keyvalue = "节点 %s 清除key %s  成功" % (self.proxyip, self.key)
            except BaseException as e:
                logger.error("删除key %s ,ERROR:%s" % (self.key, e))
                keyvalue = "ERROR:删除key值出错"

            return keyvalue

        else:
            keyvalue = "ERROR:key 不存在"

        return keyvalue



    def matchingdel(self,subnode):
        nodeip = subnode.split(":")[0]
        nodeport = subnode.split(":")[1]
        try:
            redisconn = RedisConn(nodeip, nodeport)
            delkey = redisconn.matchingdelete(self.key)

        except BaseException as e:
            logger.error(e)
            delkey = 0

        delkeysum = dict(node=subnode, delkeysum=delkey)

        return json.dumps(delkeysum)

    def TheadPool(self):
        p = Pool(processes=5)
        # 声明一个列表，用来存放各进程返回的结果
        result_list = []
        subnodelist = pullsubnode(self.proxyip,self.proxyport).subnode()
        for index in range(len(subnodelist)):
            # 将返回结果append到列表中
            result_list.append(p.apply_async(self.matchingdel, args=(subnodelist[index],)))


        p.close()
        p.join()
        # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
        results = []
        # 循环读出列表返回的结果
        for res in result_list:
            results.append(res.get())

        return results



if __name__ == '__main__':
    # pass
    test = cacheoperation
    testvalue = test("118.89.18.234","19000","nihao*").TheadPool()
    print(testvalue)



    # # test = pullsubnode
    # # print(test("118.89.18.234","19000").subnode())
    #
    # # redistable = RedisHost.objects.filter(redis_ip__exact="118.89.18.234",redis_port__exact="19000").values(
    # #     'admin_addr', 'admin_port')
    # # redisip = list(redistable)
    # #
    # #


    # print("http://%s:%s/proxy/slots" % (redisip[0]["admin_addr"],redisip[0]["admin_port"]))