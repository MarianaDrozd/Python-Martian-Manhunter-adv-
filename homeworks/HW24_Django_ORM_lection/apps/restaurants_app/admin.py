from django.contrib import admin

# Register your models here.
from restaurants_app.models import Restaurant, Personal, Country, City, Menu, Dish

admin.site.register(Restaurant)
admin.site.register(Personal)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Menu)
admin.site.register(Dish)
