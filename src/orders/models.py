from django.db import models
from user.models import User
from products.models import Product


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.BigIntegerField()
    status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    customer_address = models.TextField()
    is_paid = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} by {self.user.username}"
    
class order_item(models.Model):
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_purchase= models.BigIntegerField()

    def  __str__(self):
         return f"{self.quantity} x {self.product.name} in {self.order.id}"