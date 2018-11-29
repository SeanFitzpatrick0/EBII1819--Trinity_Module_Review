from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from modules.models import Module, Module_Comment
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Created associated profile for user
            try:
                Profile.objects.update_or_create(
                user=user
            )
            except:
                user.delete()
                pass

            userName = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for { userName }. Please Login')
            return redirect('login_page')

    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Module_Comment
    success_url = reverse_lazy('profile_page')
    template_name = 'users\module_comment_confirm_delete.html'

    def test_func(self):
        commment = self.get_object()
        if self.request.user == commment.author:
            return True
        return False
