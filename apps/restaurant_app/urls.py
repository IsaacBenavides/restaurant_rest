from django.urls import path
from .views import *
from apps.restaurant_app.api.urls import urlpatterns as api_urls


clients_urls = [
    path("list_clients/", ListClientView.as_view(), name="list_clients"),
    path("create_client/", CreateClientView.as_view(), name="create_client"),
    path("edit_client/<int:pk>/", EditClientView.as_view(), name="edit_client"),
    path("delete_client/<int:pk>/", DeleteClientView.as_view(), name="delete_client"),
]

waiter_urls = [
    path("list_waiters/", ListWaiterView.as_view(), name="list_waiters"),
    path("create_waiter/", CreateWaiterView.as_view(), name="create_waiter"),
    path("edit_waiter/<int:pk>/", EditWaiterView.as_view(), name="edit_waiter"),
    path("delete_waiter/<int:pk>/", DeleteWaiterView.as_view(), name="delete_waiter"),
]

table_urls = [
    path("list_table/", ListTableView.as_view(), name="list_table"),
    path("create_table/<int:client>", CreateTableView.as_view(), name="create_table"),
    path("edit_table/<int:pk>", EditTableView.as_view(), name="edit_table"),
]

urlpatterns = clients_urls + waiter_urls + table_urls
