#coding=utf-8
from django.template import Context,loader
from django.http import *
import md5,datetime,random,uuid
from handv.home.mail import *
from handv.home.models import * 
from django.core.paginator import *
from django.db.models import Q

def index(request): 
    return articles(request,1)

def test(request): 
    c = Context({}) 
    t = loader.get_template('test.html')
    return HttpResponse(t.render(c))

def search(request): 
    key = request.GET['key'].strip()
    if key=="":
        return result("写点关键词")
    else:
        articles = Article.objects.filter((Q(tag__icontains=key)|Q(title__icontains=key)|Q(content__icontains=key))&Q(state='01')).order_by('-addtime')
        if len(articles)==0:
            return result("没有相应的结果！") 
        c = Context({'key':key,'articles':articles,'session':request.session}) 
        t = loader.get_template('search.html')
        return HttpResponse(t.render(c))

def articles(request,page):  
    after_range_num = 5 
    bevor_range_num = 4 
    if page==None:
        page=1
    else:
        page=int(page) 
    articles = Article.objects.filter(state='01').order_by('-addtime')   
    paginator = Paginator(articles,2)  
    try:  
        articles = paginator.page(page)  
    except(EmptyPage,InvalidPage,PageNotAnInteger):  
        articles = paginator.page(1) 
    if page >= after_range_num:  
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]  
    else:  
        page_range = paginator.page_range[0:int(page)+bevor_range_num]         
    c = Context({'articles':articles,'page_range':page_range,'session':request.session}) 
    t = loader.get_template('index.html')
    return HttpResponse(t.render(c))

def photo(request):
    return photos(request,1)

def photos(request,page):  
    after_range_num = 5 
    bevor_range_num = 4 
    if page==None:
        page=1
    else:
        page=int(page) 
    photos = Attachment.objects.filter(type='00',state='01').order_by('-addtime')   
    paginator = Paginator(photos,4)  
    try:  
        photos = paginator.page(page)  
    except(EmptyPage,InvalidPage,PageNotAnInteger):  
        photos = paginator.page(1) 
    if page >= after_range_num:  
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]  
    else:  
        page_range = paginator.page_range[0:int(page)+bevor_range_num]         
    c = Context({'photos':photos,'page_range':page_range,'session':request.session}) 
    t = loader.get_template('photos.html')
    return HttpResponse(t.render(c))

def tags(request):
    tags = Tag.objects.filter(state="01")
    html =""
    for tag in tags:
        html +="<a href='/tag/"+tag.name+"'>"+tag.name+"</a>"
    return HttpResponse(html)

def tag(request,tag):
    articles = Article.objects.filter(Q(tag__icontains=tag)&Q(state='01')).order_by('-addtime')   
    c = Context({'articles':articles,'session':request.session}) 
    t = loader.get_template('tag_article.html')
    return HttpResponse(t.render(c))

def article(request,param):  
    try:
        id = int(param)
        article = Article.objects.get(id=id)
    except Exception,e:
        url=str(param)
        articles = Article.objects.filter(url=url)
        article=articles[0]
    comments = Comment.objects.filter(article=article).order_by('-addtime')
    c = Context({'article':article,'comments':comments,'session':request.session}) 
    t = loader.get_template('article.html')
    return HttpResponse(t.render(c))

def recentPosts(request):
    articles = Article.objects.filter(state='01').order_by('-addtime')   
    paginator = Paginator(articles,5)  
    articles = paginator.page(1) 
    html =""
    for article in articles.object_list:
        if article.url =="":
            html +="<a class=\"pl\" href='/article/"+article.id+"'>"+article.title+"</a>"
        else:
            html +="<a class=\"pl\" href='/article/"+article.url+"'>"+article.title+"</a>"
    return HttpResponse(html)

def recentComments(request):
    comments = Comment.objects.filter(state='01').order_by('-addtime')   
    paginator = Paginator(comments,5)  
    comments = paginator.page(1) 
    html =""
    for comment in comments.object_list:
        article = comment.article
        if article.url =="":
            html +="<a class=\"pr\" href='/article/"+article.id+"'><span class=\"prs\">"+str(comment.addtime)+"</span>"+comment.content+"</a>"
        else:
            html +="<a class=\"pr\" href='/article/"+article.url+"'><span class=\"prs\">"+str(comment.addtime)+"</span>"+comment.content+"</a>"
    return HttpResponse(html)

def register(request):  
    c = Context({}) 
    t = loader.get_template('register.html')
    return HttpResponse(t.render(c))   
 
def doRegister(request):
    username = request.POST['username'].strip()
    password = request.POST['password'].strip() 
    password1 = request.POST['password1'].strip() 
    email =request.POST['email']  
    name =request.POST['name']  
    if username=='' or password=='' or password1=='' or email=='' or name=='':
        return result("请输入完整注册信息，注册的每项都是必填地...")
    if password!=password1:
        return result("两次密码对不上啊...")
    if validateEmail(email):
        u = User.objects.filter(email=email)
        if len(u)>0:
            return result("邮箱被人用过了...")
        else:
            u = User.objects.filter(username=username)
            if len(u)>0:
                return result("用户名被人用过了...")
            else:
                password = md5.new(password)
                code = str(uuid.uuid1())
                user = User(name=name,username=username,email=email,regtime=datetime.datetime.now(),password=password.hexdigest(),state='0',internal=0,code=code)
                user.save()
                html = "请点击 <a href='http://www.handv.org/confirm?code="+code+"'>'http://www.handv.org/confirm?code="+code+"'</a>进行注册确认！"
                send_mail(email,"一休和老刘的朋友注册确认",html)
                return result("去你的邮箱查查注册确认邮件吧！")
    else:
        return result("邮箱格式不对啊！")

def findback(request):  
    c = Context({}) 
    t = loader.get_template('findback.html')
    return HttpResponse(t.render(c))   
 
def doFindback(request):
    username = request.POST['username'].strip()
    email =request.POST['email']  
    if username==''  or email=='':
        return result("请输入完整注册信息，注册的每项都是必填地...")
    u = User.objects.filter(email=email,username=username)
    if len(u)>0:
        u = u[0]
        p= str(random.randint(0,6))+str(random.randint(0,6))+str(random.randint(0,6))+str(random.randint(0,6))+str(random.randint(0,6))+str(random.randint(0,6))
        password = md5.new(p)
        u.password = password.hexdigest()
        u.save()
        html = "你的新密码是‘"+p+"’  ，请点击 <a href='http://www.handv.org/login/'>http://www.handv.org/login/</a>进行登录，赶快修改你的新密码吧！"
        send_mail(email,"一休和老刘的小窝新密码",html)
        return result("新密码已经发到你的邮箱了！")
    else:
        return result("输入的信息有误啊！")
 
def result(result):
    c = Context({'result':result}) 
    t = loader.get_template('result.html')
    return HttpResponse(t.render(c)) 

def validateEmail(email):
    if len(email) > 6:
        if re.match('^[\w\.-]+@[\w\.-]+\.\w{2,4}$', email) != None:
            return 1
    return 0

def confirm(request):
    code = request.GET['code'].strip()
    u = User.objects.filter(code=code)
    u=u[0]
    u.state='1'
    u.save()
    return result("确认成功，请<a href='/login/'>登录</a>")
