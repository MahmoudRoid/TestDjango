from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.db.models import Sum


class ProductType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Product(models.Model):
    price = models.IntegerField(verbose_name="قیمت", default=0)
    name = models.CharField(max_length=128)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'type')

    def __str__(self):
        return "{} - {}".format(self.name,self.type)


class Member(AbstractUser):
    pass


