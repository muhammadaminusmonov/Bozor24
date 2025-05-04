from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from region.models import Region

class User(AbstractUser):
    status_type = []
    role_type = []
    total_money = models.BigIntegerField(default=0)
    status = models.SmallIntegerField(choices=status_type, default=0)
<<<<<<< HEAD
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
=======
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, blank=True)
>>>>>>> db895a93631b250cb8e265dead1175fe51df9a09
    role = models.CharField(choices=role_type, default="user")

    def __str__(self):
        return self.username