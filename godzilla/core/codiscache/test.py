

import os
import  json
import django
import  requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

from godzilla.models import RedisHost
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator



def pullsubnode():
    pass




if __name__ == '__main__':
    url = "http://118.89.18.234:11080/proxy/slots"
    test = requests.get(url=url)
    jsondata = json.loads(test.content)
    # print(jsondata[0]["backend_addr"])

    testlist = []
    for i in jsondata:
      testlist.append(i["backend_addr"])

    print(set(testlist))











