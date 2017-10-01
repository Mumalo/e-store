from django.contrib import admin
from .models import Pages

class HomeAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']

class PageAdmin(admin.ModelAdmin):
    pass
    # list_display = ['title', 'photos', 'text']

admin.site.register(Pages, PageAdmin)
# admin.site.register(contact_us, ContactUsAdmin)
# admin.site.register(about_us, AboutUsAdmin)
#
#
