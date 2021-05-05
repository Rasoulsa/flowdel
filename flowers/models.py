from django.db import models
from django.db.models.fields.related import ForeignKey
from providers.models import Provider


class FlowerTypes(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.type}'


class FlowerColors(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.color}'


class FlowerOccasions(models.Model):
    occasion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.occasion}'


class Flower(models.Model):

    flower_name = models.CharField(max_length=100, blank=True, null=True)
    flower_provider = models.ManyToManyField(
        Provider, related_name="flowers")
    flower_type = models.ForeignKey(FlowerTypes, null=True,
                                    blank=True, on_delete=models.PROTECT)
    color = models.ForeignKey(FlowerColors, null=True,
                              blank=True, on_delete=models.PROTECT)
    occasion = models.ForeignKey(FlowerOccasions, null=True,
                                 blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.flower_name)
