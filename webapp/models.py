import uuid
from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Register(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=10)

    banks = models.ManyToManyField(Bank)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Journal(models.Model):

    TransactionId = models.CharField(max_length=1000, unique=True, default=uuid.uuid4)
    TimeDate = models.DateTimeField(auto_now_add=True)
    CellPhone = models.CharField(max_length=10)
    Receiver = models.CharField(max_length=50)
    DepositOption = models.CharField(max_length=3)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Success = models.BooleanField(default=False)
    Summary = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.TransactionId} - {self.Receiver}"
