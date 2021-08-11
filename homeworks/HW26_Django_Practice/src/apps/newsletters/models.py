from django.db import models


# Create your models here.
class NewsLetter(models.Model):
    email = models.EmailField(max_length=75, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'News Letter'
        verbose_name_plural = 'News Letters'
