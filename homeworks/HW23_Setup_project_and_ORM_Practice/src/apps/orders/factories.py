import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Name'
    last_name = 'Surname'
    email = 'name.surname@gmail.com'
    phone = '+380670101010'
    car_id = 1
