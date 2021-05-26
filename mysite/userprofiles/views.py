from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import (
    LogoutView as BaseLogoutView
)

class LogInView(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'


class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'logout.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

def home(request):
    return render(request, 'home.html')