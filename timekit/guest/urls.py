from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.usersubmit, name='usersubmit'),
    url(r'^calender1/', views.calender1, name='calender1'),
    url(r'^calender/$',views.usercalender, name='usercalender'),
    url(r'^auth1/$',views.auth, name='auth1'),
    url(r'^auth/$',views.userauth, name='userauth'),
    # url(r'^findtime/$',views.findtime, name='findtime'),
    # url(r'^webpage/$', views.webpage, name='webpge'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^signup/user/$', views.signup, name='signup'),

]
