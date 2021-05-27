from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse 
from django.db.models.signals import post_save
from django.conf import settings

class UserProfileManager(models.Manager):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(
                User, 
                on_delete=models.CASCADE, 
                unique=True,
                related_name='userprofile'
        )
    location = models.CharField(default=None,
        max_length=50, blank=False)
    number = models.IntegerField(default=None)
    amka = models.IntegerField(default=None)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('userprofiles:profile')#, kwargs={'slug':self.slug})

