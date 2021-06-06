from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import *

def upload(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()

            messages.success(request, f'Your contact has been created!')

    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'registration/upload.html', context)