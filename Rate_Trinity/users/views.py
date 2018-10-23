from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for { userName }.')
            return redirect('homepage')
        else: 
            error_message = ''
            feilds_errors = [ (field.label, field.errors) for field in form]
            for feild in feilds_errors:
                if feild[1] != '':
                    error_message = error_message + feild[1]

            messages.warning(request, f'Unable to create user. Your form is not valid.\
             Please correct the following issues:{error_message}')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form})
