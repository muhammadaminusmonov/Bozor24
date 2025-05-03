from django.db import models
from user.models import User


class Payment(models.Model):
    method_choice = [
        (1, "Online Transaction"),
        (2, "ATM")
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0)
    payment_at = models.DateTimeField(auto_now_add=True)
    method = models.CharField(choices=method_choice, default=1)

    def __str__(self):
        return self.amount