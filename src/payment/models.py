from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()

class Payment(models.Model):
    method_choice = [
        ('1', "Online Transaction"),
        ('2', "ATM")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)
    payment_at = models.DateTimeField(auto_now_add=True)
    method = models.CharField(choices=method_choice, default=1)

    def __str__(self):
        return str(self.amount)

class Transaction(models.Model):
    status_choice = [
        (1, "Pending"),
        (2, "Processing"),
        (3, "Completed"),
        (4, "Canceled")
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.BigIntegerField(null=False, blank=False)
    status = models.SmallIntegerField(choices=status_choice, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)
