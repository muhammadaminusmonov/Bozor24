from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class User(AbstractUser, AbstractBaseUser):
    status_type = []
    total_money = models.BigIntegerField(default=0)
    status = models.SmallIntegerField(choices=status_type, default=0)

    def __str__(self):
        return self.username
