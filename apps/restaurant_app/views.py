from .models import *
from .forms import *
from django.shortcuts import render, redirect

from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

# ============== Client Views =================


class ListClientView(ListView):

    model = Client
    template_name = "client/client_list.html"
    context_object_name = "clients"


class CreateClientView(CreateView):

    template_name = "client/create_client.html"
    form_class = ClientForm
    model = Client
    success_url = "/list_clients/"
    waiter = Waiter.objects.all().first()
    table = Table.objects.all().first()

    def post(self, request, *args, **kwargs):
        self.waiter = Waiter.objects.filter(id_waiter=request.POST.get("waiter"))
        self.table = Table.objects.filter(id_table=request.POST.get("table"))
        return super().post(request, *args, **kwargs)

    def get_success_url(self) -> str:
        print(self.waiter.first())
        print(self.table.first())
        return super().get_success_url()


class EditClientView(UpdateView):
    template_name = "client/edit_client.html"
    form_class = ClientForm
    model = Client
    success_url = "/list_clients/"


class DeleteClientView(DeleteView):
    template_name = "client/delete_client.html"
    model = Client
    success_url = "/list_clients/"


# ============== Waiter Views =================


class ListWaiterView(ListView):

    model = Waiter
    template_name = "waiter/waiter_list.html"
    context_object_name = "waiters"


class CreateWaiterView(CreateView):

    template_name = "waiter/create_waiter.html"
    form_class = WaiterForm
    model = Waiter
    success_url = "/list_waiters/"


class EditWaiterView(UpdateView):
    template_name = "waiter/edit_waiter.html"
    form_class = WaiterForm
    model = Waiter
    success_url = "/list_waiters/"


class DeleteWaiterView(DeleteView):
    template_name = "waiter/delete_waiter.html"
    model = Waiter
    success_url = "/list_waiters/"


# ============== Table Views =================


class ListTableView(ListView):

    model = Table
    context_object_name = "tables"
    template_name = "table/table_list.html"


class CreateTableView(CreateView):

    template_name = "table/create_table.html"
    form_class = TableForm
    model = Table
    success_url = "/list_table/"

    def get_form_kwargs(self):
        kwargs = super(CreateTableView, self).get_form_kwargs()
        print(self.kwargs)
        return kwargs


class EditTableView(UpdateView):
    template_name = "table/edit_table.html"
    form_class = TableForm
    model = Table
    success_url = "/list_table/"


class DeleteWaiterView(DeleteView):
    template_name = "table/delete_table.html"
    model = Table
    success_url = "/list_table/"
