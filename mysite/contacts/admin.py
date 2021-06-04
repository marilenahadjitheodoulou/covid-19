from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'name', 'email', 'number', 'date', 'details')
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)