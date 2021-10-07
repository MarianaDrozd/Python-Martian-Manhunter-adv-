import django.utils.timezone
from django.contrib.auth import get_user_model
from django.db import models

AUTH_USER_MODEL = get_user_model()


# Create your models here.


class Car(models.Model):
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
    )

    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        null=True
    )

    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
    )
    engine_type = models.CharField(
        max_length=75,
        default=0,
    )

    POLLUTANT_CLASS_Aa = "class A+"
    POLLUTANT_CLASS_A = "class A"
    POLLUTANT_CLASS_B = "class B"
    POLLUTANT_CLASS_C = "class C"
    POLLUTANT_CLASS_D = "class D"
    POLLUTANT_CLASS_E = "class E"
    POLLUTANT_CLASS_F = "class F"
    POLLUTANT_CLASS_G = "class G"

    POLLUTANT_CLASS_CHOICES = (
        (POLLUTANT_CLASS_Aa, "A+"),
        (POLLUTANT_CLASS_A, "A"),
        (POLLUTANT_CLASS_B, "B"),
        (POLLUTANT_CLASS_C, "C"),
        (POLLUTANT_CLASS_D, "D"),
        (POLLUTANT_CLASS_E, "E"),
        (POLLUTANT_CLASS_F, "F"),
        (POLLUTANT_CLASS_G, "G"),
    )
    pollutant_class = models.CharField(
        max_length=30,
        choices=POLLUTANT_CLASS_CHOICES,
        default=POLLUTANT_CLASS_Aa,
        blank=True
    )

    price = models.PositiveIntegerField(default=0)

    fuel_type = models.CharField(max_length=75)

    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending Car Sell"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    slug = models.SlugField(max_length=75)

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        blank=True
    )
    doors = models.SmallIntegerField(default=4)

    capacity = models.PositiveIntegerField(default=0)

    gear_case = models.CharField(max_length=75)

    number = models.CharField(max_length=30)

    sitting_place = models.PositiveSmallIntegerField(default=4)

    first_registration_date = models.DateTimeField(default=django.utils.timezone.now)

    engine_power = models.PositiveIntegerField(default=0)

    picture = models.ForeignKey('cars.Picture', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машини"

    def __str__(self):
        return self.slug


class Color(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Model(models.Model):
    brand = models.ForeignKey('cars.Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Property(models.Model):
    CATEGORY_0 = 'Quadricycle'
    CATEGORY_A = 'Mini'
    CATEGORY_B = 'Small'
    CATEGORY_C = 'Medium'
    CATEGORY_D = 'Large'
    CATEGORY_E = 'Executive'
    CATEGORY_F = 'Luxury'
    CATEGORY_S = 'Sports coupes'
    CATEGORY_M = 'Multi purpose'
    CATEGORY_J = 'Sport utility'

    CATEGORY_CHOICES = (
        (CATEGORY_0, 'Quadricycle'),
        (CATEGORY_A, 'Mini'),
        (CATEGORY_B, 'Small'),
        (CATEGORY_C, 'Medium'),
        (CATEGORY_D, 'Large'),
        (CATEGORY_E, 'Executive'),
        (CATEGORY_F, 'Luxury'),
        (CATEGORY_M, 'Multi purpose'),
        (CATEGORY_J, 'Sport utility'),
    )

    name = models.CharField(max_length=75)
    category = models.CharField(
        max_length=75,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_0,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Picture(models.Model):
    url = models.ImageField(
        upload_to='pictures',
        null=True,
        blank=True,
    )
    position = models.IntegerField()
    metadata = models.TextField()

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'
