from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

# Asosiy abstract comment modeli
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    writed_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

# Mahsulot uchun izohlar
class CommentProduct(Comment):
    product = models.ForeignKey(Product, related_name='comment_product', on_delete=models.CASCADE)

    def __str__(self):

        return f"Comment by {self.user.username} on {self.product.name}"

# Foydalanuvchi (sotuvchi) uchun izohlar
class CommentUser(models.Model):
    seller = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on seller: {self.seller.username}"

