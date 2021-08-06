from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

USER_MODEL = get_user_model()

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.ForeignKey(
        'restaurants_app.City',
        on_delete=models.CASCADE,
    )
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
    )
    menu = models.ManyToManyField(
        'restaurants_app.Menu'
    )

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Ресторани"

    def __str__(self):
        return f'{self.name}'


class Personal(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    home = models.CharField(max_length=50)
    restaurant = models.ForeignKey(
        'restaurants_app.Restaurant',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Країна"
        verbose_name_plural = "Країни"

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(
        'restaurants_app.Country',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Місто"
        verbose_name_plural = "Міста"

    def __str__(self):
        return f'{self.name}'


class Menu(models.Model):
    SPRING = 'Spring'
    SUMMER = 'Summer'
    AUTUMN = 'Autumn'
    WINTER = 'Winter'
    DEFAULT = 'Default'

    SEASON_MENU_CHOICES = [
        (SUMMER, 'Summer menu'),
        (AUTUMN, 'Autumn menu'),
        (WINTER, 'Winter menu'),
        (SPRING, 'Spring menu'),
        (DEFAULT, 'Default menu'),
    ]
    menu = models.CharField(
        max_length=15,
        choices=SEASON_MENU_CHOICES,
        default=DEFAULT,
    )

    dishes = models.ManyToManyField(
        'restaurants_app.Dish',
        related_name='dishes'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return f'{self.menu}'


class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = ArrayField(
        models.CharField(max_length=25, blank=True),
    )
    is_ok_for_vegans = models.BooleanField(default=False)
    description = models.TextField()
    price = models.PositiveIntegerField(editable=True)
    menu = models.ManyToManyField(
        'restaurants_app.Menu',
        related_name='menues',
    )
    place = models.ManyToManyField(
        'restaurants_app.Restaurant',
        related_name='dishes',
    )

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'

    def __str__(self):
        return f'{self.name}'

