from django.conf.urls import url
from . import views	
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^Signup',views.signup),
    url(r'^register$', views.registor),
    url(r'^homepage$',views.homepage),
    url(r'^login$',views.loginaccount),
    url(r'^logout$',views.logout),
    url(r'^post$',views.post),
    url(r'^edit/(?P<id>\d+)$', views.editaccount),
    url(r'^editmyaccount/(?P<id>\d+)$', views.editmyaccount),
    url(r'^postacomment$',views.post_a_comment),
    url(r'^myaccount/(?P<id>\d+)$', views.viewmyaccount),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    # url(r'^editpost/(?P<id>\d+)$', views.editpost),
    url(r'^right/(?P<id>\d+)$', views.rightanswer),
    url(r'^wrong/(?P<id>\d+)$', views.wronganswer),
    url(r'^viewthisacc/(?P<id>\d+)/(?P<id2>\d+)$', views.viewthisacc),
    url(r'^notes/(?P<id>\d+)/(?P<id2>\d+)$',views.notes),
    
]