from django.urls import path
from . import views
from userprofiles import views as userprofiles_views

app_name='userprofiles'
urlpatterns = [
    path('', userprofiles_views.home, name='home'),
    path('register/', userprofiles_views.register, name='register'),
    path('profile/', userprofiles_views.ProfileView.as_view(), name='profile'),
    path('edit_profile/', userprofiles_views.ProfileUpdateView.as_view(), name='edit_profile'),
]