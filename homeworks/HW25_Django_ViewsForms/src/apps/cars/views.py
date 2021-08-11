from django.core import serializers
from django.http import HttpResponse
from apps.cars.models import Car
from django.views.generic import ListView, DetailView


class CarsListView(ListView):
    model = Car.objects.all()
    context_object_name = 'cars'
    template_name = 'cars/list.html'

    def get_queryset(self):
        return Car.objects.all()


class CarsDetailView(DetailView):
    model = Car
    context_object_name = 'cars'
    slug_url_kwarg = 'car_slug'
    template_name = 'cars/detail.html'


def serialized_cars(request):
    data = serializers.serialize('json', Car.objects.all())
    return HttpResponse(request.method + '<br>' + data)
