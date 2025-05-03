from django.db import models
from django.contrib.auth.models import User
from region.models import Region
from category.models import Category

class Product(models.Model):
    STATUS_CHOICES = [
        (1, "Available For Sale"),
        (2, "Out of Stock")
    ]
    title = models.CharField(max_length=255)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    discount = models.IntegerField(null=True, blank=True)
    discount_limit_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.TextField()

    def __str__(self):
        return f"Image for {self.product.title}"

class PromotedProduct(models.Model):
    status_choice = [
        (1, "Active"),
        (2, "Inactive")
    ]

    PROMO_TYPES = (
        (1, 'Basic'),
        (2, 'Popular'),
        (3, 'Special'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promo_type = models.CharField(max_length=50, choices=PROMO_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    status = models.SmallIntegerField(choices=status_choice, default=2)
    view_limit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.title} - {self.promo_type}"
