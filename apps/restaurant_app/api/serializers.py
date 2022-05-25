from rest_framework import serializers
from apps.restaurant_app.models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["name", "observations"]


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ["name", "last_name"]


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ["num_diners", "ubications"]


class SaucerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saucer
        fields = ["name", "amount"]


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ["name", "amount"]


class InvoiceSerializer(serializers.ModelSerializer):

    client = ClientSerializer()
    waiter = WaiterSerializer()
    table = TableSerializer()

    class Meta:
        model = Invoice
        fields = ["date", "client", "waiter", "table"]


class OrderSerializer(serializers.ModelSerializer):

    saucers = SaucerSerializer()
    drinks = DrinkSerializer()
    invoice = InvoiceSerializer()

    class Meta:
        model = Order
        fields = ["saucers", "drinks", "invoice"]
