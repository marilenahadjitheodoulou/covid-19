from django import forms
from django.contrib.auth.models import User
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'number', 'date', 'details')
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.number = self.cleaned_data['number']
        user.date = self.cleaned_data['date']        
        user.details = self.cleaned_data['details']
    
        if commit:
            user.save()
        return user