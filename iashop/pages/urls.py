
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about_us/$', views.about_us, name='about'),
    url(r'^contact_us/$', views.contact_us, name='contact'),
    url(r'^make_money/$', views.make_money, name='make-money'),
    url(r'^partner/$', views.partner, name='partner'),
    url(r'^advertise/$', views.advertise, name='advertise'),
    url(r'^help/$', views.help, name='help'),


    # url()
]