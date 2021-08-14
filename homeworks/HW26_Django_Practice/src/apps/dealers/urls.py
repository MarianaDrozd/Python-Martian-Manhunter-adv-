from django.urls import path

from apps.dealers.views import DealersListView, DealersDetailView, serialized_dealers

app_name = 'dealers'

urlpatterns = [
    path(
        '',
        DealersListView.as_view(),
        name='dealer_list',
    ),
    path(
        '<int:dealer_pk>/',
        DealersDetailView.as_view(),
        name='dealer_detail',
    ),
    path(
        'api/car/json/',
        serialized_dealers,
    )
]
