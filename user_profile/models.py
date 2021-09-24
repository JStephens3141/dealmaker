from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_broker = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=True)
    broker_name = models.CharField(max_length=200)
    broker_address = models.CharField(max_length=200)
    broker_license_id = models.CharField(max_length=20)
    
class BrokerAgent(models.Model):
    broker_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='%(class)s_brokerAgent_id')
    agent_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='%(class)s_agentBroker_id')

