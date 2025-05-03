from django.db import models

class Attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    category_id = models.foreignkey('Category', on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

def __str__(self):
    return self.attribute_name

class product_attribute(models.Model):
    product_attribute_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute_id = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

def __str__(self):
    return self.value

