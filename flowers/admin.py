from django.contrib import admin
from .models import Flower, FlowerTypes, FlowerColors, FlowerOccasions

admin.site.register(Flower)
admin.site.register(FlowerTypes)
admin.site.register(FlowerColors)
admin.site.register(FlowerOccasions)
