from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from .manage import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[
        phone_regex], max_length=17, blank=False, null=False, unique=True)  # validators should be a list

    slug = models.SlugField(max_length=255, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # def save(self, *args, **kwargs):
    #     slug = slugify(self.phone)
    #     self.slug = slug
    #     super().save(*args, **kwargs)
