from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    preview = models.ImageField(upload_to='post_previews', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    """references"""
    category = models.ManyToManyField(Category, related_name="products")

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


"""DATE_FIELD = YYYY-MM-DD"""
"""DATETIME_FIELD = YYYY-MM-DD HH:mm:ss:ms"""
