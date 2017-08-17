from django.contrib import admin
from .models import Institution,Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'photo', 'phone', 'institution', 'gender', 'bio']

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'zip_code']

# class NotificationAdmin(admin.ModelAdmin):
#     exclude = []


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Profile, ProfileAdmin)

# Register your models here.
