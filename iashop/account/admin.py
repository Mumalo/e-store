from django.contrib import admin
from .models import Profile, State


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'photo', 'phone', 'state', 'local_govt_area ', 'gender', 'bio']

class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'zip_code']

# class NotificationAdmin(admin.ModelAdmin):
#     exclude = []


# admin.site.register(Sate, InstitutionAdmin)
# admin.site.register(Profile, ProfileAdmin)

# Register your models here.
