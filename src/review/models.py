from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='reviews')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=[(i, str(i)) for i in range(1, 6)], default=1,help_text="1 dan 5 gacha baho")

    def __str__(self):
        return f"{self.user}  {self.product}  {self.rating}"
