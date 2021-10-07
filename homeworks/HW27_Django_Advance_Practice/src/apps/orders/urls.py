from django.urls import path

from apps.orders.views import OrdersListView, OrdersDetailView, serialized_orders

app_name = 'orders'

urlpatterns = [
    path(
        '',
        OrdersListView.as_view(),
        name='order_list',
    ),
    path(
        '<int:order_pk>/',
        OrdersDetailView.as_view(),
        name='order_detail',
    ),
    path(
        'api/order/json/',
        serialized_orders,
    )
]
