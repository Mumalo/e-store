from django.contrib import admin
from .models import Pages, Team, TeamMember

class HomeAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']

class PageAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    exclude = ['title']

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'fb_page_url', 'tw_page_url', 'inst_page_url']
    # list_display = ['title', 'photos', 'text']

admin.site.register(Pages, PageAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
# admin.site.register(contact_us, ContactUsAdmin)
# admin.site.register(about_us, AboutUsAdmin)
#
#
