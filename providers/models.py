from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
# from .manage import CustomProviderManager


class Provider(models.Model):

    owner_name = models.CharField(max_length=100, blank=False, null=False)
    providername = models.CharField(
        max_length=255, blank=False, null=False, unique=True)

    # phone
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[
        phone_regex], max_length=17, blank=False, null=False, unique=True)  # validators should be a list

    # address
    address_city = models.CharField(max_length=50, blank=False, null=False)
    address_street1 = models.CharField(max_length=100, blank=False, null=False)
    address_street2 = models.CharField(max_length=100, blank=False, null=False)
    address_zipcode = models.CharField(max_length=50, blank=False, null=False)

    # password
    password = models.CharField(max_length=200, null=False, blank=False)

    def save(self):
        self.password = make_password(self.password)
        super(Provider, self).save()

    # objects = CustomProviderManager()

    def __str__(self):
        return str(self.providername)
