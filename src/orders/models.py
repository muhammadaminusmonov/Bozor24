from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
User = get_user_model()


class Order(models.Model):
    STATUS_TYPES = [
        (1, ""),
    ]
    PAYMENT_METHOD = [
        (1, "Bozor24 account"),
        (2, "Pay in received")
    ]
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.BigIntegerField(null=False, blank=False)
    status = models.SmallIntegerField(choices=STATUS_TYPES, default=1)
    payment_method = models.CharField(choices=PAYMENT_METHOD)
    customer_address = models.TextField(choices=STATUS_TYPES)
    is_paid = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_purchase = models.BigIntegerField()

    def __str__(self):
        return f"{self.order} , {self.product.title}"