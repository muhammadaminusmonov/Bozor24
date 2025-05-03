from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    status_type = []
    total_money = models.BigIntegerField(default=0)
    status = models.SmallIntegerField(choices=status_type, default=0)

    def __str__(self):
        return self.username
