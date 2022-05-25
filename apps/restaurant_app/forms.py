from http import client
from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    waiter = forms.ModelChoiceField(
        queryset=Waiter.objects.all(),
        widget=forms.Select(attrs={"class": "form-control", "name": "waiter"}),
    )
    table = forms.ModelChoiceField(
        queryset=Table.objects.all(),
        widget=forms.Select(attrs={"class": "form-control", "name": "table"}),
    )
    observations = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Client
        fields = ["name", "waiter", "table", "observations"]


class WaiterForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Waiter
        fields = ["name", "last_name"]


class TableForm(forms.ModelForm):

    num_diners = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}), label="Dinners"
    )
    ubications = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Table
        fields = ["num_diners", "ubications"]


class DrinkForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )


class SaucerForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )


class InvoiceForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    waiter = forms.ModelChoiceField(queryset=Waiter.objects.all())
    table = forms.ModelChoiceField(queryset=Table.objects.all())


class OrderForm(forms.ModelForm):

    drinks = forms.ModelChoiceField(queryset=Drink.objects.all())
    saucers = forms.ModelChoiceField(queryset=Saucer.objects.all())

    def __init__(self, *args, **kwargs):
        client = kwargs.pop("client")
        queryset = Invoice.objects.all()
        if client:
            queryset = Invoice.object.filter(
                client=Client.objects.get(id_client=client)
            )

        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields["invoice"] = forms.ModelChoiceField(queryset=queryset)
