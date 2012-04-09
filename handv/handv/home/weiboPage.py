#coding=utf-8
import datetime,time    
import getpass
import os
import sys
import md5
import json
import random
from weibo import APIClient
from django.template import Context, loader,RequestContext
from django.db.models import Q
from django.http import *
from handv.home.models import * 
from handv.home.page import *

#handv.org的app key
#App Key:
#4063812394
#App Secret:
#52af8800f00298516c88a0f2be95a65a

#现在使用的是jad系统消息借口的app_key和app_secret
APP_KEY = '2945318614' # app key of betball
APP_SECRET = '26540ac5e2728be53005df042bc9bc00' # app secret of betball
CALLBACK_URL = 'http://127.0.0.1:8888/weiboLoginBack' # callback url
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
SITE_URL = 'http://www.handv.org'

def weiboLogin(request):
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    return HttpResponseRedirect(url) 

def weiboBack(request):
    #得到微博认证的信息
    code = request.GET['code']
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in
    # TODO: 在此可保存access token
    request.session['access_token'] = access_token
    request.session['expires_in'] = expires_in
    client.set_access_token(access_token, expires_in)
    #测试发微博
#    status = u'亲们，俺刚才手快，测试了一把，您别b4啊！'
#    client.post.statuses__update(status=status)
    #得到微博用户的id，如果有绑定，则直接登录，没有则跳到绑定页面
    json_obj = client.get.statuses__user_timeline()
    weibo_user = json_obj['statuses'] [0]['user']
    #得到用户的weibo UID
    weibo = weibo_user['id']
#    request.session['weibo_client'] = client
    request.session['weibo'] = weibo
    #得到用户的微博nick
    weibo_nick = weibo_user['screen_name']
    request.session['weibo_nick'] = weibo_nick
    m = User.objects.filter(weibo=weibo,internal=0) 
    if len(m)!=0:
        user = m[0]
        request.session['user'] = user
        user.weibo_nick=weibo_nick
        user.save()
        return HttpResponseRedirect("/home")
    else:
        c = Context({'info':'请先登陆绑定帐号先','session':request.session}) 
        t = loader.get_template('login.html')
        return HttpResponse(t.render(c))

def bind(request): 
    m = User.objects.filter(username=request.POST['username'])      
    pwd = md5.new(request.POST['password'])
    pwd.digest()
    if len(m)!=0:
        if  m[0].password == pwd.hexdigest():
            user = m[0]
            request.session['user'] = user
            weibo = request.session['weibo']
            user.weibo = weibo
            user.save() 
            return result("绑定成功.")
        else:
            return result("伊用户名密码错了。。先注册下吧.")
    else:
        return result("伊用户名密码错了。。先注册下吧.")      
