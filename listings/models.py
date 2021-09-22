from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility

class listing(models.Model):
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField(max_length=5)
    nickname = models.CharField(max_length=50)
    square_feet = models.IntegerField(max_length=5)
    image = models.CharField(max_length=100)
    asking_price = models.IntegerField(max_length=8)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
