
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^account/register/$', views.user_registration, name='register'),
    url(r'^account/login/$', views.user_login, name='login'),
    url(r'^account/home/follow/$', views.user_follow, name='follow'),
    url(r'^account/home/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^account/logout/$', views.logout_user, name='logout'),
    url(r'^account/edit/$', views.edit_profile, name='edit'),
]