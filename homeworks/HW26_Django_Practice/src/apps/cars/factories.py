import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    number = 'AA 1111 AA'
    slug = 'bla-bla'
    engine_power = 150
    dealer_id = 2
    color_id = 2
    model_id = 2
    picture_id = 2


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'blue'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'bmw'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'sedan'
