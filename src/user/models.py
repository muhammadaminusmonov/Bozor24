from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from region.models import Region

class User(AbstractUser):
    status_type = [
        (0, "Inactive"),
        (1, "Active"),
    ]

    ROLE_USER = "user"
    ROLE_ADMIN = "admin"
    role_type = [
        (ROLE_USER, "User"),
        (ROLE_ADMIN, "Admin"),
    ]

    total_money = models.BigIntegerField(default=0)
    status = models.SmallIntegerField(choices=status_type, default=0)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(choices=role_type, default="user")
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    follow_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.seller.username}"
