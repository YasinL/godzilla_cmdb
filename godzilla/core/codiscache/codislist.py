

import os
import  json
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
django.setup()
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

from godzilla.models import RedisHost
from godzilla.core.Log import logger
from godzilla.handle.decorator_login import login_decorator


def redislist(request):
    if request.method == "POST":
        pass
    else:
        return  render_to_response('codis-list.html')
