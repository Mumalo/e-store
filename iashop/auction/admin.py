from django.contrib import admin
from .models import  Category, AuctionEvent, Bid, SubCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description']
    prepopulated_fields = {'slug':('name',)}
    # readonly_fields = {'slug', ('name',)}

class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id','time','item', 'category', 'sub_category', 'target_price', 'start_price', 'start_time', 'end_time', 'creator', 'description', 'available']

class BidAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'bidder', 'event']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'category', 'name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(AuctionEvent, AuctionAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)




# Register your models here.
