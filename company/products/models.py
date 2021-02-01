from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    description = models.TextField(max_length=500)