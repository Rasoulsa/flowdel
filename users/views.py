from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/users_register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:register')
    success_message = "%(phone)s was created successfully"
