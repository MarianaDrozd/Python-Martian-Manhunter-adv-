from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# Create your views here.
from apps.dealers.models import Dealer


class DealersListView(ListView):
    model = Dealer.objects.all()
    context_object_name = 'dealers'
    template_name = 'dealers/list.html'

    def get_queryset(self):
        return Dealer.objects.all()


class DealersDetailView(DetailView):
    model = Dealer
    context_object_name = 'dealers'
    pk_url_kwarg = 'dealer_pk'
    template_name = 'dealers/detail.html'


def serialized_dealers(request):
    data = serializers.serialize('json', Dealer.objects.all())
    return HttpResponse(request.method + '<br>' + data)
