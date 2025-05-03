from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    add_category_at = models.DateTimeField(auto_now_add=True)
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    def __str__(self):
        return self.name

