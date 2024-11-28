from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from . import forms, models

class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

class AuthLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("users:user_list")

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

class UserListView(ListView):
    model = models.CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"  
