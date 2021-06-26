from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, CenterDetails

class UserProfileAdmin(admin.ModelAdmin):
  
    list_display = ('user', 'location', 'phonenumber', 'amka')
    class Meta:
        model = UserProfile

class CenterDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    
    class Meta:
        model = CenterDetails

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CenterDetails, CenterDetailsAdmin)
