from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.fields import DateTimeField

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, help_text='Enter a valid email address')
    number = models.IntegerField(default=None)
    date = models.IntegerField(default=None)
    details = models.CharField(max_length=50)

    def __str__(self):
        return self.user