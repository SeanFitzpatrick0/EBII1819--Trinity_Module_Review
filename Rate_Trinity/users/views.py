from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from modules.models import Module
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for { userName }. Please Login')
            return redirect('login_page')

    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')