from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm, UserLoginForm


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/users_register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:register')
    success_message = "%(phone)s was created successfully"

    def get_context_data(self, *args, **kwargs):
        data = super(RegisterView, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Register'
        return data


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/users_login.html'
    form_class = UserLoginForm
    success_message = "%(username)s was login successfully"


def get_context_data(self, *args, **kwargs):
    data = super(CustomLoginView, self).get_context_data(*args, **kwargs)
    data['page_title'] = 'Log In'
    return data
