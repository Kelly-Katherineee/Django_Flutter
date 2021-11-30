import json

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import request
from django.views import View

from Django_operate import models
from Django_operate.models import UserInfo, Users


def login(request):
    if request.method == "POST":
        postbody = request.body
        data = json.loads(postbody.decode())
        if data:
            # usercode = data['usercode']
            code = data['code']
            password = data['password']
            # print(code, password)
            try:
                # use = Users.objects.get(usercode=usercode)
                # print(password, use.password)
                # 确认账户（手机号/密码）存在
                if Users.objects.get(phone=code):
                    use = Users.objects.get(phone=code)
                    # print(password, use.phone)
                    # 密码正确性判断
                    if check_password(password, use.password):
                        # request.session['is_login'] = True
                        # request.session['usercode'] = usercode
                        # request.session['password'] = password
                        return JsonResponse(data, safe=False)
                    else:
                        return JsonResponse({'errmsg': 'Password error'})
                elif Users.objects.get(email=code):
                    use = Users.objects.get(email=code)
                    # print(password, use.email)
                    # 密码正确性判断
                    if check_password(password, use.password):
                        # request.session['is_login'] = True
                        # request.session['usercode'] = usercode
                        # request.session['password'] = password
                        return JsonResponse(data, safe=False)
                    else:
                        return JsonResponse({'errmsg': 'Password error'})
            except:
                return JsonResponse({'errmsg': 'Password error'})
            else:
                return JsonResponse({'errmsg': 'No user'})


def register_phone(request):
    if request.method == "Get":
        return HttpResponse(request, "ok")
    if request.method == "POST":
        postbody = request.body
        data = json.loads(postbody.decode())
        # email = data['email']
        phone = data['phone']
        password = data['password']
        # if Users.objects.filter(email=email):
        #     return HttpResponse('该邮箱号已经注册')
        if Users.objects.filter(phone=phone):
            return HttpResponse('该手机号已经注册')
        else:
            user = Users()
            # user.email = email
            user.phone = phone
            user.password = password
            user.save()
    return JsonResponse(data, safe=False)


def register_email(request):
    if request.method == "Get":
        return HttpResponse(request, "ok")
    if request.method == "POST":
        postbody = request.body
        data = json.loads(postbody.decode())
        email = data['email']
        password = data['password']
        # if Users.objects.filter(email=email):
        #     return HttpResponse('该邮箱号已经注册')
        if Users.objects.filter(email=email):
            return HttpResponse('该邮箱已经注册')
        else:
            user = Users()
            user.email = email
            user.password = password
            user.save()
    return JsonResponse(data, safe=False)
