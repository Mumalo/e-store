from django.contrib import admin
from .models import  Category, AuctionEvent, Bid

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description']
    # readonly_fields = {'slug', ('name',)}

class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id','time','item', 'category', 'target_price', 'start_price', 'start_time', 'end_time', 'creator', 'description', 'available']

class BidAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'bidder', 'event']


admin.site.register(Category, CategoryAdmin)
admin.site.register(AuctionEvent, AuctionAdmin)
admin.site.register(Bid, BidAdmin)




# Register your models here.
