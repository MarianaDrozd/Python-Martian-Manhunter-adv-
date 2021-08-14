from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

# Create your views here.
from apps.orders.models import Order


class OrdersListView(ListView):
    model = Order.objects.all()
    context_object_name = 'orders'
    template_name = 'orders/list.html'

    def get_queryset(self):
        return Order.objects.all()


class OrdersDetailView(DetailView):
    model = Order
    context_object_name = 'orders'
    pk_url_kwarg = 'order_pk'
    template_name = 'orders/detail.html'


def serialized_orders(request):
    data = serializers.serialize('json', Order.objects.all())
    return HttpResponse(request.method + '<br>' + data)
