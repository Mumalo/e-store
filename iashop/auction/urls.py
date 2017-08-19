
from django.conf.urls import url
app_name = 'auction'

from . import views

urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'^auction/add/$', views.add_new_auction, name='add_new_auction'),
     url(r'^auction/list/$', views.auction_list, name='list'),
     url(r'^auction/(?P<auction_id>[0-9]+)/bid/$', views.auction_detail, name='bid'),
     url(r'^auction/(?P<auction_id>[0-9]+)/edit/$', views.edit_auction, name='edit_auction'),
     url(r'^budget/create/$', views.create_budget_plan, name='budget'),
     url(r'^advert/create/$', views.create_advert, name='advert'),


]


