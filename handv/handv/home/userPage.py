#coding=utf-8
from django.template import Context,loader
from django.http import HttpResponse
from handv.home.models import * 
import logging
import md5
from handv.home.page import *
logger = logging.getLogger(__name__)

def interceptor(func):
    logger.info('interceptor function : %s ' % func.__name__);
    def wapper(request,*args,**kargs):
        if 'user' in request.session and request.session['user']:
            try:
                response =  func(request,*args,**kargs)
                return response
            except Exception,e:
                print e
                return HttpResponse("error"+str(e))
        else:
            return login(request)
    return wapper

def login(request):  
    c = Context({'result':'You must login!'}) 
    t = loader.get_template('login.html')
    return HttpResponse(t.render(c))

def logout(request):  
    try:
        request.session.clear();
    except KeyError:
        pass
    return result("注销成功！")

@interceptor
def add(request):  
    now = datetime.datetime.now()
    tags = Tag.objects.all()
    c = Context({'now':now,'tags':tags,'session':request.session}) 
    t = loader.get_template('add.html')
    return HttpResponse(t.render(c))

@interceptor
def saveAdd(request):
    title = request.POST['title']
    tag = request.POST['tag']
    url = request.POST['url']
    content = request.POST['content']
    now = datetime.datetime.now()
    user = request.session['user']
    article = Article(user=user,addtime=now,url=url,content=content,title=title,tag=tag,state='01',type='00')
    article.save()  
    return result("发表成功！")

@interceptor
def addTag(request):
    name = request.GET['name'].strip()  
    tags = Tag.objects.filter(name=name)
    user = request.session['user']
    if len(tags)==0:
        tag = Tag(name=name,user=user,desc='',type='00')
        tag.save()
        return HttpResponse(name)
    else:
        return HttpResponse("error")

def doLogin(request):  
    username = request.POST['username']
    password = request.POST['password']
    if username=='' or password=='':
        return result("请输入用户名或者密码！")
    m = User.objects.filter(username=username,internal=0)      
    pwd = md5.new(request.POST['password'])
    pwd.digest()
    if len(m)!=0:
        if  m[0].password == pwd.hexdigest():
            if m[0].state=='0':
                return result("帐号没有激活。请先登录邮箱或者联系一休激活帐号。")
            else:
                try:
                    request.session['user'] = m[0]
                    weibo = request.session['weibo']
                    if weibo!=None and weibo!='':
                        user = m[0]
                        user.weibo =weibo
                        user.save()
                        return result("绑定成功！")
                except KeyError:
                    pass
                return home(request)
        else:
            return result("用户名或者密码错拉！")
    else:
        return result("用户名或者密码错拉！")
    
@interceptor
def home(request):  
    user = request.session['user']
    c = Context({'user':user,'session':request.session}) 
    t = loader.get_template('home.html')
    return HttpResponse(t.render(c))