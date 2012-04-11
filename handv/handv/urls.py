from django.conf.urls.defaults import *
from handv.home.page import *
from handv.home.userPage import *
from handv.home.weiboPage import *
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',  index),  
    (r'^home/',  home),  
    (r'^test/',  test), 
    (r'^register/',  register),  
    (r'^doRegister/',  doRegister),  
    (r'^findback/',  findback),  
    (r'^doFindback/',  doFindback),  
    (r'^confirm/',  confirm),  
    (r'^article/(\w+)/$', article),
    (r'^articles/(\w+)/$', articles),
    (r'^photos/(\w+)/$', photos),
    (r'^photo/', photo),
    (r'^login/', login),
    (r'^logout/', logout),
    (r'^doLogin/', doLogin),
    (r'^weiboLogin/', weiboLogin),
    (r'^weiboLoginBack/', weiboBack),
    (r'^weiboJsBack/', weiboJsBack),
    (r'^add/', add),
    (r'^addArticle/', addArticle),
    (r'^saveEdit/', saveEdit),
    (r'^upload/', upload),
    (r'^doUpload/', doUpload),
    (r'^tags/', tags),
    (r'^recentPosts/', recentPosts),
    (r'^recentComments/', recentComments),
    (r'^addComment/', addComment),
    (r'^tag/(\w+)/$', tag),
    (r'^addTag/', addTag),
    (r'^articleAdmin/', articleAdmin),
    (r'^commentAdmin/', commentAdmin),
    (r'^delComment/(\w+)/$', delComment),
    (r'^tagAdmin/', tagAdmin),
    (r'^delTag/(\w+)/$', delTag),
    (r'^delArticle/(\w+)/$', delArticle),
    (r'^editArticle/(\w+)/$', editArticle),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(globals()["__file__"]) + '/html/css'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(globals()["__file__"]) + '/html/images'}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(globals()["__file__"]) + '/html/js'}),
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(globals()["__file__"]) + '/home/files'}),
      
    # Example:
    # (r'^handv/', include('handv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
