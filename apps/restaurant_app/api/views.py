from rest_framework import viewsets, permissions, generics
from .serializers import *


class ClientViewSet(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateClientView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class WaiterViewSet(generics.ListAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateWaiterView(generics.CreateAPIView):
    serializer_class = WaiterSerializer
    queryset = Waiter.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class TableViewSet(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateTableView(generics.CreateAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class SaucerViewSet(generics.ListAPIView):
    queryset = Saucer.objects.all()
    serializer_class = SaucerSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateSaucerView(generics.CreateAPIView):
    serializer_class = SaucerSerializer
    queryset = Saucer.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class DrinkViewSet(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateDrinkView(generics.CreateAPIView):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class InvoiceViewSet(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateInvoiceView(generics.CreateAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
