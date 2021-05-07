from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['phone', 'password']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    pass
