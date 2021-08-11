
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(max_length=100)

    email = models.EmailField(
        max_length=50,
        unique=True
    )

    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
        default=''
    )

    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
    )

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=40)

    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
        related_name='cities',
        default=''
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=40)

    code = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
