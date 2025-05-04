from django.contrib.auth.models import AbstractUser
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)
    parent_region = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subregions')
    add_region_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name