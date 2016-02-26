from django.db import models
from django.contrib.auth.models import User
from event.models import event
from society.models import *
from billing.models import billing

Male = 'M'
    Female = 'F'
    gender_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),
    )

class AdUser(User):
    dob= models.DateField(auto_now=True, auto_now_add=True)	
    occupation= models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices = gender_CHOICES)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None)
    flat_f = society.models.ForeignKey(Flat,unique=True)
    event_f = event.models.ForeignKey(Event,unique=True) 
    billing_f = billing.models.ForeignKey(Billing,unique=True)
