from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from region.models import Region

class User(AbstractUser):
    status_type = []
    role_type = []
    total_money = models.BigIntegerField(default=0)
    status = models.SmallIntegerField(choices=status_type, default=0)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    role = models.CharField(choices=role_type, default="user")

    def __str__(self):
        return self.username