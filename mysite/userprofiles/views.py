from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from userprofiles.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm, UserProfileForm, EditProfileForm, EditProForm
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView
)

class LogInView(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'


class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'logout.html'


def home(request):
    count = User.objects.count()
    context = {'count': count}
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            login(request, user)

            return redirect('userprofiles:profile')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/register.html', context)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

class ProfileCreateView(CreateView):
    model = UserProfile
    fields = ['location', 'number', 'amka']
    template_name = 'registration/edit_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreateView, self).form_valid(form)

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    form = EditProfileForm
    profile_form = EditProForm
    template_name = 'registration/edit_profile.html'

    def post(self, request):
        
        form = EditProfileForm(request.POST or None, instance=request.user)
        #userprofile = UserProfile.objects.filter(id=request.user.id).first()
        #if not getattr(request.user,'userprofile'):
        #    return redirect('create_profile')  

        profile_form = EditProForm(request.POST or None, instance=request.user.userprofile) 
            
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('userprofiles:profile')

        context = self.get_context_data(
            form=form,
            profile_form=profile_form
        )

        return self.render_to_response(context)   

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)