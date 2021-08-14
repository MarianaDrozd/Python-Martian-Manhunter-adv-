from django.contrib import admin

# Register your models here.
from apps.cars.models import Car, Color, Brand, Model, Property, Picture

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Property)
admin.site.register(Picture)
