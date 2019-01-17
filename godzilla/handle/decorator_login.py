
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from godzilla.handle.permission import check_permiss
from godzilla.models import users
from godzilla.models import role
from godzilla.models import permission
from godzilla.models import memuid
from godzilla.models import memulist


def permission_check(username):
    memuidlist = []
    roleid = users.objects.filter(username__exact=username).values('roleid')
    permissiontable = permission.objects.filter(roleid__exact=roleid).values('permission_id')

    for permissionid  in permissiontable:
        fatmemu = memulist.objects.filter(permission_id=permissionid["permission_id"]).values()

        memu = list(fatmemu)
        permission_url = memu[0]["permission_url"]
        memuidlist.append(permission_url.split("/")[2])

    return memuidlist







'''
装饰器 登录验证
'''
def login_decorator(func):
    def check_login(request):
        username = request.session.get('username')
        permission = permission_check(username)
        path = request.path.split("/")[2]
        if username is not None and path in permission:
            return func(request)

        else:
            return HttpResponseRedirect('/godzilla/index')

    return check_login




# def login_check_permission(func):
#     def check_login(request):
#         username = request.session.get('username')
#         permission = check_permiss(username)
#         path =  request.path.split("/")[2]
#         if username is not None:
#             for per in permission:
#                 permission_url = per.permission_url
#                 if path == permission_url.path.split("/")[2]:
#                     return func(request)
#                 break
#
#             return HttpResponseRedirect('/godzilla/index')
#         else:
#             return HttpResponseRedirect('/godzilla/index')
#
#     return check_login

if __name__ == '__main__':
    print(check_permiss("admin"))