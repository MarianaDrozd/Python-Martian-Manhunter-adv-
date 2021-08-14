from apps.cars.views import CarsListView, CarsDetailView, serialized_cars
from django.urls import path

app_name = 'cars'

urlpatterns = [
    path(
        '',
        CarsListView.as_view(),
        name='car_list',
    ),
    path(
        '<slug:car_slug>/',
        CarsDetailView.as_view(),
        name='car_detail',
    ),
    path(
        'api/car/json/',
        serialized_cars,
    )
]
