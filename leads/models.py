from django.db import models


class Lead(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=10)
    propertiesShown = models.PositiveIntegerField(default=0)


class Brokerage(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    licensee_name = models.CharField(max_length=200)


class Agent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    broker = models.CharField(max_length=200)
