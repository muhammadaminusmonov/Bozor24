from django.db import models
from user.models import User
from products.models import Product


class Orders(models.Model):
    STATUS_TYPES = [
        (1, ""),
    ]
    PAYMENT_METHOD = [
        (1, "Bozor24 account"),
        (2, "Pay in received")
    ]
    status = models.CharField()
    payment_method = models.CharField(choices=PAYMENT_METHOD)
    customer_address = models.TextField(choices=STATUS_TYPES)
    is_paid = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_purchase= models.BigIntegerField()

    def  __str__(self):
         return f"{self.quantity} x {self.product.name} in {self.order.id}"