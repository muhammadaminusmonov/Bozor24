from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"Item {self.product.title} in Cart {self.cart.id}"