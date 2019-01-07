
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect


'''
装饰器 登录验证
'''
def login_decorator(func):
    def check_login(request):
        username = request.session.get('username')
        if username is not None:
            return func(request)
        else:
            return HttpResponseRedirect('/godzilla/index')

    return check_login