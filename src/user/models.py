from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from region.models import Region

class User(AbstractUser):
    status_type = [
        (0, "Inactive"),
        (1, "Active"),
    ]

    role_type = [
        ("user", "User"),
        ("admin", "Admin"),
    ]

    total_money = models.BigIntegerField(default=0)
    status = models.SmallIntegerField(choices=status_type, default=0)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True) # bu siz testcaselar ishlamayabdi
    role = models.CharField(max_length=10, choices=role_type, default="user")

    def __str__(self):
        return self.username
