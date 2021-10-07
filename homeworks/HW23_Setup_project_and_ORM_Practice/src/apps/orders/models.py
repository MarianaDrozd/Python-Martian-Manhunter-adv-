from django.db import models
from phone_field import PhoneField


# Create your models here.
class Order(models.Model):
    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = PhoneField
    message = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
