from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
  
    list_display = ('user', 'location', 'number', 'amka')
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
