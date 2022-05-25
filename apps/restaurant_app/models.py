from django.db import models


class Client(models.Model):
    id_client = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=45, null=False, blank=False)
    observations = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name


class Waiter(models.Model):
    id_waiter = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=45, null=False, blank=False)
    last_name = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.last_name}"


class Table(models.Model):

    id_table = models.AutoField(primary_key=True, editable=False)
    num_diners = models.IntegerField(null=False, blank=False, default=0)
    ubications = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return str(self.id_table)


class Saucer(models.Model):

    id_saucer = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=45, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name


class Drink(models.Model):

    id_drink = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=45, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name


class Invoice(models.Model):

    id_invoice = models.AutoField(primary_key=True, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=False, blank=False
    )
    waiter = models.ForeignKey(
        Waiter, on_delete=models.CASCADE, null=False, blank=False
    )
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.id_invoice)


class Order(models.Model):

    drinks = models.ForeignKey(Drink, on_delete=models.CASCADE)
    saucers = models.ForeignKey(Saucer, on_delete=models.CASCADE)
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, null=False, blank=False
    )
