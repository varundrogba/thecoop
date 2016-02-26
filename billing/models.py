from django.db import models
from django.contrib.auth.models import User
from event.models import event
from society.models import *
from aduser.models import aduser

class Billing(models.Model):
    bill_name = models.CharField(max_length=60)
    bill_type = models.CharField(max_length=1, choices = bill_CHOICES)
    bill_amtpaid = models.PositiveSmallIntegerField(99999)
    bill_amtpending = models.PositiveSmallIntegerField(99999)
    bill_totalamt = models.PositiveSmallIntegerField(99999)
    bill_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
    
