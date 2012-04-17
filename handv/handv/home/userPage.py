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
            response =  func(request,*args,**kargs)
            return response
        else:
            return login(request)
    return wapper

def weiboInterceptor(func):
    logger.info('interceptor function : %s ' % func.__name__);
    def wapper(request,*args,**kargs):
        if 'user' in request.session and request.session['user'] :
            response =  func(request,*args,**kargs)
            return response
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
    tags = Tag.objects.filter(state="01")
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
        user = request.session['user']
        attachment  = Attachment(user=user,filepath=filepath,addtime=datetime.datetime.now(),state='01',type="00")
        attachment.save()
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
    if url!="":
        articles = Article.objects.filter(url=url,state='01')
        if len(articles)>0:
            return result("url被使用过了！")
    if title=="" or content=="":
        return result("没有标题或内容啊！") 
    now = datetime.datetime.now()
    user = request.session['user']
    article = Article(user=user,addtime=now,url=url,content=content,title=title,tag=tag,state='01',type='00')
    atts = att.split(',')
    article.save()  
    for filepath in atts:
        attachment  = Attachment.objects.filter(filepath=filepath)[0]
        attachment.article=article
        attachment.save()
    return result("发表成功！")
    
@interceptor
def saveEdit(request):
    id = int(request.POST['id'])
    title = request.POST['title']
    att = request.POST['atts']
    tag = request.POST['tag']
    url = request.POST['url']
    content = request.POST['content']
    if url!="":
        articles = Article.objects.filter(url=url,state='01').exclude(id=id)
        if len(articles)>0:
            return result("url被使用过了！")
    if title=="" or content=="":
        return result("没有标题或内容啊！") 
    article = Article.objects.get(id=id) 
    user = request.session['user']
    article.tag = tag
    article.title = title
    article.url = url
    article.content = content
    atts = att.split(',')
    article.save()  
    for filepath in atts:
        attachment  = Attachment(article=article,user=user,filepath=filepath,addtime=datetime.datetime.now(),type="00")
        attachment.save()
    return result("修改成功！")

@interceptor
def addTag(request):
    name = request.GET['name'].strip()  
    tags = Tag.objects.filter(name=name,state='01')
    user = request.session['user']
    if len(tags)==0:
        tag = Tag(name=name,user=user,desc='',type='00',state='01')
        tag.save()
        return HttpResponse(name+','+str(tag.id))
    else:
        return HttpResponse("error")

def doLogin(request):  
    username = request.POST['username']
    password = request.POST['password']
    if username=='' or password=='':
        return result("请输入用户名或者密码！")
    m = User.objects.filter(username=username)      
    pwd = md5.new(request.POST['password'])
    pwd.digest()
    if len(m)!=0:
        user = m[0]
        if  user.password == pwd.hexdigest():
            if user.state=='0':
                return result("帐号没有激活。请先登录邮箱或者联系一休激活帐号。")
            else:
                request.session['user'] = user
                if user.internal==1:
                    return HttpResponseRedirect("/home")
                else:
                    try:
                        weibo = request.session['weibo']
                        if weibo!=None and weibo!='':
                            user.weibo =weibo
                            user.save()
                            return result("绑定成功！")
                    except KeyError:
                        return HttpResponseRedirect("/")  
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
    
@interceptor
def articleAdmin(request):  
    page = 1
    try:
        page = int(request.POST['page']) 
    except Exception:
        pass
    after_range_num = 5 
    bevor_range_num = 4 
    articles = Article.objects.filter(state='01').order_by('-addtime')   
    paginator = Paginator(articles,20)  
    try:  
        articles = paginator.page(page)  
    except(EmptyPage,InvalidPage,PageNotAnInteger):  
        articles = paginator.page(1) 
    if page >= after_range_num:  
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]  
    else:  
        page_range = paginator.page_range[0:int(page)+bevor_range_num]         
    c = Context({'articles':articles,'page_range':page_range,'session':request.session}) 
    t = loader.get_template('admin_article.html')
    return HttpResponse(t.render(c))

@interceptor
def commentAdmin(request):  
    page = 1
    try:
        page = int(request.POST['page']) 
    except Exception:
        pass
    after_range_num = 5 
    bevor_range_num = 4 
    comments = Comment.objects.filter(state='01').order_by('-addtime')   
    paginator = Paginator(comments,20)  
    try:  
        comments = paginator.page(page)  
    except(EmptyPage,InvalidPage,PageNotAnInteger):  
        comments = paginator.page(1) 
    if page >= after_range_num:  
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]  
    else:  
        page_range = paginator.page_range[0:int(page)+bevor_range_num]         
    c = Context({'now':datetime.datetime.now(),'comments':comments,'page_range':page_range,'session':request.session}) 
    t = loader.get_template('admin_comment.html')
    return HttpResponse(t.render(c))
  
@interceptor
def tagAdmin(request):  
    tags = Tag.objects.filter(state="01")
    c = Context({'now':datetime.datetime.now(),'tags':tags,'session':request.session}) 
    t = loader.get_template('admin_tag.html')
    return HttpResponse(t.render(c))
  
@interceptor
def editArticle(request,id):  
    id = int(id)
    article = Article.objects.get(id=id) 
    hadTags = article.tag.split(' ')
    tags = Tag.objects.filter(state="01")
    comments = Comment.objects.filter(article=article).order_by('-addtime')
    c = Context({'article':article,'tags':tags,'hadTags':hadTags,'comments':comments,'session':request.session}) 
    t = loader.get_template('edit.html')
    return HttpResponse(t.render(c))

@interceptor
def delArticle(request,id):  
    id = int(id)
    article = Article.objects.get(id=id) 
    article.state='02'
    article.save()
    return HttpResponse("删除成功！")

@interceptor
def delTag(request,id):  
    id = int(id)
    tag = Tag.objects.get(id=id)
    tag.state='02'
    tag.save()
    return HttpResponse("删除成功！")

@interceptor
def delComment(request,id):  
    id = int(id)
    article = Comment.objects.get(id=id) 
    article.state='02'
    article.save()
    return HttpResponse("删除成功！")

@interceptor
def photoAdmin(request):  
    page = 1
    try:
        page = int(request.POST['page']) 
    except Exception:
        pass
    after_range_num = 5 
    bevor_range_num = 4 
    photos = Attachment.objects.all().order_by('state','-addtime')   
    paginator = Paginator(photos,20)  
    try:  
        photos = paginator.page(page)  
    except(EmptyPage,InvalidPage,PageNotAnInteger):  
        photos = paginator.page(1) 
    if page >= after_range_num:  
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]  
    else:  
        page_range = paginator.page_range[0:int(page)+bevor_range_num]         
    c = Context({'now':datetime.datetime.now(),'photos':photos,'page_range':page_range,'session':request.session}) 
    t = loader.get_template('admin_photo.html')
    return HttpResponse(t.render(c))

@interceptor
def delPhoto(request,id,type):  
    type = str(type)
    id = int(id)
    photo = Attachment.objects.get(id=id) 
    if type=="0":
        photo.state='02'
        photo.save()
    else:
        filepath = os.path.dirname(globals()["__file__"])+photo.filepath
        os.remove(filepath)
        photo.delete() 
    return HttpResponse("删除成功！")  

from django import forms
class UploadFileForm(forms.Form):
    fileToUpload = forms.FileField()
