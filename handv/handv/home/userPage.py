#coding=utf-8
from django.template import Context,loader
from django.http import HttpResponse
from handv.home.models import * 
import logging
import md5
from handv.home.page import *
from django.conf import settings

logger = logging.getLogger(__name__)

def interceptor(func):
    logger.info('interceptor function : %s ' % func.__name__);
    def wapper(request,*args,**kargs):
        if 'user' in request.session and request.session['user'] and request.session['user'].internal==1:
            try:
                response =  func(request,*args,**kargs)
                return response
            except Exception,e:
                print e
                return HttpResponse("error"+str(e))
        else:
            return login(request)
    return wapper

def weiboInterceptor(func):
    logger.info('interceptor function : %s ' % func.__name__);
    def wapper(request,*args,**kargs):
        if 'user' in request.session and request.session['user'] :
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
def upload(request):  
    now = datetime.datetime.now()
    c = Context({'now':now,'session':request.session}) 
    t = loader.get_template('upload.html')
    return HttpResponse(t.render(c))

@interceptor
def doUpload(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        f = request.FILES['fileToUpload']
        filepath = handle_uploaded_file(f)
        return HttpResponse("{msg:'"+filepath+"'}")
    else:
        return HttpResponse("{error:'没有文件和描述啊大姐'}")

def handle_uploaded_file(f):
    now = datetime.datetime.now()
    filedir = "/files/"+str(now.year)+"/"+str(now.month)+"/"
    filename=filedir+str(uuid.uuid1())+f.name
    fname = os.path.dirname(globals()["__file__"])+filename
    if os.path.exists(fname):  #判断文件夹是否存在
        os.remove(fname)
    dirs= os.path.dirname(fname)  #如果fname是完整路径 则输出完整的 否则为空
    if not os.path.exists(dirs):  #判断这个路径是否存在
        os.makedirs(dirs)   #如果不存在则创建这个目录
    if os.path.isfile(fname):  #判断是否为文件，是true,不是False,
        os.remove(fname) 
    fp = open(fname, 'wb')  #读写打开这个要上传的文件
    for content in f.chunks(): #写
        fp.write(content)
    fp.close()
    return filename
    
@interceptor
def addArticle(request):
    title = request.POST['title']
    att = request.POST['atts']
    tag = request.POST['tag']
    url = request.POST['url']
    content = request.POST['content']
    if title=="" or content=="":
        return result("没有标题或内容啊！") 
    now = datetime.datetime.now()
    user = request.session['user']
    article = Article(user=user,addtime=now,url=url,content=content,title=title,tag=tag,state='01',type='00')
    atts = att.split(',')
    article.save()  
    for filepath in atts:
        attachment  = Attachment(article=article,user=user,filepath=filepath,addtime=datetime.datetime.now(),type="00")
        attachment.save()
    return result("发表成功！")

@interceptor
def addTag(request):
    name = request.GET['name'].strip()  
    tags = Tag.objects.filter(name=name)
    user = request.session['user']
    if len(tags)==0:
        tag = Tag(name=name,user=user,desc='',type='00',state='00')
        tag.save()
        return HttpResponse(name)
    else:
        return HttpResponse("error")

def doLogin(request):  
    username = request.POST['username']
    password = request.POST['password']
    if username=='' or password=='':
        return result("请输入用户名或者密码！")
    m = User.objects.filter(username=username,internal=1)      
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
                return HttpResponseRedirect("/home")
        else:
            return result("用户名或者密码错拉！")
    else:
        return result("用户名或者密码错拉！")
    
@interceptor
def home(request):  
    user = request.session['user']
    now = datetime.datetime.now()
    c = Context({'user':user,'now':now,'session':request.session}) 
    t = loader.get_template('home.html')
    return HttpResponse(t.render(c))

@weiboInterceptor
def addComment(request):  
    user = request.session['user']
    articleId = request.POST['articleId']
    article = Article.objects.get(id=int(articleId))
    content = request.POST['content']
    if content =="":
        return result("哥们填点评论内容啊！")
    else:
        comment = Comment(user=user,article=article,addtime=datetime.datetime.now(),title="",content=content,state='00')
        comment.save()
        return result("发表成功啦！")
    
from django import forms
class UploadFileForm(forms.Form):
    fileToUpload = forms.FileField()
