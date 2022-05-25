from django.urls import path
from .views import *


urlpatterns = [
    path("clients/", ClientViewSet.as_view(), name="clients"),
    path("client/create/", CreateClientView.as_view(), name="create_client"),
    path("waiters/", WaiterViewSet.as_view(), name="waiters"),
    path("waiter/create/", CreateWaiterView.as_view(), name="create_waiter"),
    path("tables/", TableViewSet.as_view(), name="tables"),
    path("table/create/", CreateTableView.as_view(), name="create_table"),
    path("saucers/", SaucerViewSet.as_view(), name="saucers"),
    path("saucer/create/", CreateSaucerView.as_view(), name="create_saucer"),
    path("drinks/", DrinkViewSet.as_view(), name="drinks"),
    path("drink/create/", CreateDrinkView.as_view(), name="create_drink"),
    path("invoices/", InvoiceViewSet.as_view(), name="orders"),
    path("invoice/create/", CreateInvoiceView.as_view(), name="create_order"),
    path("orders/", OrderViewSet.as_view(), name="orders"),
    path("order/create/", CreateOrderView.as_view(), name="create_order"),
]
