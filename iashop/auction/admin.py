from django.contrib import admin
from .models import  Advert, Category, AuctionEvent, Bid


class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description']

class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id','time','item', 'category', 'target_price', 'start_price', 'start_time', 'end_time', 'creator', 'status', 'description']

class BidAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'bidder', 'event']


admin.site.register(Advert, AdvertAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AuctionEvent, AuctionAdmin)
admin.site.register(Bid, BidAdmin)




# Register your models here.
