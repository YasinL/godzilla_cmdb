#!/usr/bin/env python
# -*- conding:utf-8 -*-
__Author__ = "Yasin Li"

import redis
import json
import datetime

class RedisConn(object):
    def __init__(self,redisip,redisport,):
        # pool = redis.ConnectionPool(host=redisip, port=redisport)
        # self.__conn = redis.StrictRedis(connection_pool=pool)
        self.__conn = redis.Redis(host=redisip,port=redisport)
        # decode_responses = True

    def get(self,key):
        if self.__conn.exists(key):
            return self.__conn.get(key)
        else:
            return "Error"

    def set(self,*args):
        self.__conn.set(*args)

    def delete(self,key):
        self.__conn.delete(key)

    def llen(self,key):
        self.llen(key)
    def exists(self,key):
        return  self.__conn.exists(key)

    def keys(self):
        return self.__conn.keys()

    def matchingdelete(self,key):
        return  self.__conn.delete(*self.__conn.keys(key))



if __name__ == '__main__':
    # pass
    # pool = redis.ConnectionPool(host='118.89.18.234', port=6379, db=0)
    # r = redis.StrictRedis(connection_pool=pool)
    #
    # keys = r.exists("test")
    # print(type(keys))
    #
    # print(keys)

    redisconn = RedisConn(redisip='118.89.18.234',redisport=6379)
    keyvalue = redisconn.matchingdelete("nihao_*")
    # eyvalue = keyvalue.decode("ISO-8859-1")
    print(keyvalue)
    # print(redisconn.exists("IOP_MARKET_EXPOSURE_HOME_POP_2018071915_1234567"))
    # value = redisconn.get("11")
    # print(value)
    # v = str(value,encoding="utf8")
    # print(v)
    # ss = '\xac\xed\x00\x05t\x00\x02ON'
    # a = ss.encode()
    # b = a.decode()
    # print(b)
    # redisconn.set("111111","22222222","100")
    # keys = redisconn.keys()
    # print(keys)
    # if redisconn.delete('test') is  None:
    #     print("yes")
    # else:
    #     print("no")
# print(redisconn.delete('test'))
# print(redisconn.matchingdelete("*TEST*"))
# redisconn.get('123')
# redisconn.set('nihao','sdadasdasdas')
# value = [1635995, 8699230, 4885, 7090, 3055, 15, 4020, 0, 0, 5960, 0, 0, 0, 3055, 0, 0, 15, 0, 4015, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0]
# print(type(value))
# redisconn.set('ngx_value',value)
#
# # print(redisconn.exits("ngx_value").decode("utf-8"))
# print(json.loads(redisconn.get('ngx_value')))