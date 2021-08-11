import factory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Country'

    name = 'Ukraine'


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.City'

    name = 'Lviv'
    country_id = 2


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Dealer'

    title = 'my_dealer'
    e_mail = 'mydealer@mail.com'
    user_id = 3
    city_id = 1
