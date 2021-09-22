from django.db import models
from django.db.models.base import Model


class Lead(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    cellphone = models.CharField(max_length=10)
    other_phone = models.CharField(max_length=10)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    best_contact_time = models.TimeField()
    preferred_contact_method = models.CharField(max_length=5)


    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)