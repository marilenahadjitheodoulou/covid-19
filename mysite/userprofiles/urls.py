from django.urls import path
from . import views
from userprofiles import views as userprofiles_views

app_name='userprofiles'
urlpatterns = [
    path('', userprofiles_views.home, name='home'),
    path('profile/', userprofiles_views.ProfileView.as_view(), name='profile'),
]