from django.db import models
from authenticate.models import User


class Product(models.Model):
    title = models.CharField(max_length=256)
    merchant = models.ManyToManyField(User)
    price = models.FloatField()
    description = models.CharField(max_length=512)
    pin_code = models.IntegerField()
    address = models.CharField(max_length=256)
