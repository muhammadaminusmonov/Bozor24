from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    writed_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CommentProduct(Comment):
    product = models.ForeignKey(Product, related_name='comment_product', on_delete=models.CASCADE)  # Ideally should be a ForeignKey to a Product model

    def __str__(self):
        def __str__(self):
            return f"Product Comment: {self.id}"


class CommentUser(models.Model):
    seller = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)  # Ideally should be a ForeignKey to a Seller model

    def __str__(self):
        def __str__(self):
            return f"Product Comment: {self.id}"

