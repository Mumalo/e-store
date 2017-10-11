from django.contrib import admin
from .models import  Category, AuctionEvent, Bid, SubCategory, WatchList, ItemOfTheDay, SubCategory2, BudgetPlan

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'image','description', 'slug']
    prepopulated_fields = {'slug':('name',)}
    # readonly_fields = {'slug', ('name',)}

class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id','time','item', 'category', 'sub_category', 'sub_category2','target_price', 'start_price', 'start_time', 'end_time', 'creator', 'description', 'available']

class BidAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'bidder', 'event']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'category', 'name']
    prepopulated_fields = {'slug': ('name',)}

class SubCategory2Admin(admin.ModelAdmin):
    list_display = [ 'id', 'sub_category', 'name']
    prepopulated_fields = {'slug': ('name',)}

class BudgetPlanAdmin(admin.ModelAdmin):
    pass



class WatchListAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'creator']
    # prepopulated_fields = {'slug': ('name',)}

class ItemOfTheDayAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'user']

admin.site.register(ItemOfTheDay, ItemOfTheDayAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AuctionEvent, AuctionAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SubCategory2, SubCategory2Admin)
admin.site.register(WatchList, WatchListAdmin)
admin.site.register(BudgetPlan, BudgetPlanAdmin)


# Register your models here.
