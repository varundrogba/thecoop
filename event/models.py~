from django.db import models
from django.contrib.auth.models import User
from society.models import *
from billing.models import billing
from aduser.models import aduser



Official = 'O'
    Normal = 'N'
    event_CHOICES = (
        (Official, 'Official'),
        (Normal, 'Normal'),
    )


class Event(models.Model):
    event_name = models.CharField(max_length=60)
    event_venue = models.CharField(max_length=100)
    event_desc = models.CharField(max_length=500)
    event_owner = models.CharField(max_length=30)
    event_type =  = models.CharField(max_length=1, choices = event_CHOICES)
    event_dtime = models.DateTimeField(auto_now=True, auto_now_add=True)

