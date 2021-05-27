from django.forms.models import model_to_dict
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/users_register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:register')
    success_message = "%(phone)s was created successfully"


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/users_login.html'
    form_class = UserLoginForm
    success_message = "%(username)s is login successfully"


class UserProfileView(LoginRequiredMixin, DetailView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'users/users_profile.html'

    def get_object(self):
        return self.request.user
