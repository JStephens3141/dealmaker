from django.db import models
from django.db.models.base import Model


class Lead(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=10)
    propertiesShown = models.PositiveIntegerField(default=0)

