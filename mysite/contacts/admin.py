from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'name', 'email', 'phonenumber', 'date', 'details')
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)