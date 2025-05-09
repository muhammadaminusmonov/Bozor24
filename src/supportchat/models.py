from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class SupportChatRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Support Chat Room #{self.id} - {self.user.username}"


class SupportMessage(models.Model):
    room = models.ForeignKey(SupportChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_support_messages')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} at {self.sent_at}"
