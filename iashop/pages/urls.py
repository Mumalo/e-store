
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about_us/$', views.about_us, name='about'),
    url(r'^contact_us/$', views.contact_us, name='contact')

    # url()
]