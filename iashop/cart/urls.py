from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^watch/$', views.add_to_watch_list, name='watch'),

]