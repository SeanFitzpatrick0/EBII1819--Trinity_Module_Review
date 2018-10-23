from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url('register/', views.register, name='register_page'),
    url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_page'),
    url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_page'),
    url('profile/', views.profile, name='profile_page')
]