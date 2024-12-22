from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=100)