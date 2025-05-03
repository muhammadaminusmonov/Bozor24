# from django.db import models
#
# class User(models.Model):
#     status_choices = []
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     last_login = models.DateTimeField(null=True, blank=True)
#     data_joined = models.DateTimeField(auto_now_add=True)
#     total_money = models.BigIntegerField(default=0)
#     status = models.SmallIntegerField(choices=status_choices, default=1)
#
#     def __str__(self):
#         return self.username