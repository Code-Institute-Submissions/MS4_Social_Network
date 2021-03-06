from django.db import models


# Product models
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/donation', null=True, blank=True)

    def __str__(self):
        return self.name
