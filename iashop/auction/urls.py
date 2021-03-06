
from django.conf.urls import url
app_name = 'auction'
# from dal import autocomplete
from .models import Category
from . import views


urlpatterns = [
     url(r'^auction/add/$', views.add_new_auction, name='add_new_auction'),
     # url(r'^auction/add/$', views.AuctionCreateView.as_view(), name='add_new_auction'),
     # url(r'^subcategory-autocomplete/$', SubCategoryAutoComplete.as_view(model=SubCategory), name='subcategory-autocomplete'),
     url(r'^auction/list/$', views.auction_list, name='list'),
     url(r'^subcat-select/$', views.select_by_category, name='select-by-category'),
     url(r'^auction/(?P<auction_id>[0-9]+)/detail/$', views.auction_detail, name='bid'),
     url(r'^auction/(?P<auction_id>[0-9]+)/edit/$', views.edit_auction, name='edit_auction'),
     url(r'^auction/(?P<auction_id>[0-9]+)/$',views.edit_auction, name='edit_item'),


     url(r'^notifications/mark-all/$', views.mark_all_as_read, name='mark-all-as-read'),
     url(r'^notifications/mark/$', views.mark, name='mark-as-read'),


     url(r'^budget/create/$', views.create_budget_plan, name='budget'),
     url(r'^budget/delete/$', views.delete_view, name='delete_budget'),
     url(r'^budget/(?P<budget_id>[0-9]+)/edit/$', views.update_budget, name='edit_budget'),
     url(r'^advert/create/$', views.create_advert, name='advert'),


#      Categories
     url(r'^category/all/$', views.all_categories, name='all_categories'),
     url(r'^category/(?P<category_id>[0-9]+)/(?P<category_slug>[-\w]+)/$', views.category_detail, name='category_detail'),
     url(r'^subcat/(?P<subcat_id>[0-9]+)/(?P<subcat_slug>[-\w]+)/$', views.subcat_detail, name='subcat_detail'),
     url(r'^(?P<subcat_id>[0-9]+)/(?P<subcat_slug>[-\w]+)/$', views.subcat2_detail, name='subcat2_detail'),
     url(r'^subcat-select2/$', views.select_by_subcat, name='select-by-subcat'),
     url(r'^subcats-cats/$', views.sub_cats_for_cats, name='subcats-for-cats'),




]


