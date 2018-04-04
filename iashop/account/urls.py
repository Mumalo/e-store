
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^account/register/$', views.user_registration, name='register'),
    url(r'^account/login/$', views.user_login, name='login'),
    url(r'^account/user/follow/$', views.user_follow, name='follow'),
    url(r'^account/user/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    # url(r'^budget/$', views.budget_reply_form, name='budget_reply'),
    url(r'^account/logout/$', views.logout_user, name='logout'),
    url(r'^account/edit/user/(?P<pk>[0-9]+)$', views.edit_profile, name='edit'),

    #smart select for state
    url(r'^account/edit/lgas-for-state/$', views.lgas_for_state, name='lgas-for-state'),

    # password change and reset views
    url(r'^account/password-change/$',auth_views.password_change,name='password_change'),
    url(r'^account/password-change/done/$',auth_views.password_change_done,name='password_change_done'),

    url(r'^password-reset/$',auth_views.password_reset,name='password_reset'),
    url(r'^password-reset/done/$',auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$',auth_views.password_reset_complete,name='password_reset_complete'),
]