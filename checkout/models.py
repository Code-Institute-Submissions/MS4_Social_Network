from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Order(models.Model):

    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)
    order = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.user, self.product.name, self.product)
