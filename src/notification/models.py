from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

class Follow(models.Model):
    # The user who is following
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    # The user being followed (seller)
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # when the follow occurred

    class Meta:
        # ensure a user can't follow the same person twice
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followed'], name='unique_follow')
        ]
        # index to speed up lookups of follow relationships
        indexes = [
            models.Index(fields=['follower', 'followed']),
        ]

class Notification(models.Model):
    # The user who receives the notification
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notifications'
    )
    message = models.TextField()  # notification message content
    timestamp = models.DateTimeField(auto_now_add=True)  # when notification was created
    # optional link to the product that triggered this notification


    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    class Meta:
        # index to speed up fetching notifications for a user in time order
        indexes = [
            models.Index(fields=['recipient', 'timestamp']),
        ]