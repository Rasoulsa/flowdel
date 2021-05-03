from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from .manage import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[
        phone_regex], max_length=17, blank=False, null=False, unique=True)  # validators should be a list

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
