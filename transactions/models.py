from django.db import models
from users.models import CustomUser
from providers.models import Provider
from flowers.models import Flower


class Transaction(models.Model):

    payer = models.ForeignKey(
        CustomUser, related_name='transactions', on_delete=models.PROTECT)
    provider = models.ForeignKey(
        Provider, related_name='transactions', on_delete=models.PROTECT)
    items = models.ManyToManyField(
        Flower, related_name='transactions')
    fee = models.IntegerField(blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.id)
