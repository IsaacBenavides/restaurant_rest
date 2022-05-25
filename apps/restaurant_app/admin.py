from django.contrib import admin
from .models import Client, Waiter, Saucer, Drink, Table, Invoice, Order


admin.site.register(Client)
admin.site.register(Waiter)
admin.site.register(Saucer)
admin.site.register(Drink)
admin.site.register(Table)
admin.site.register(Invoice)
admin.site.register(Order)
