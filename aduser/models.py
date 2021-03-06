from django.db import models
from django.contrib.auth.models import User	
#from event.models import Event
#from society.models import Flat
#from society.models import Society
#from society.models import Building
#from billing.models import Billing

Male = 'M'
Female = 'F'
gender_CHOICES = (
(Male, 'Male'),
(Female, 'Female'),
)

class AdUser(models.Model):
    dob= models.DateField(auto_now=True, auto_now_add=True)	
    occupation= models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices = gender_CHOICES)
    photo = models.ImageField(upload_to='/images/', height_field=None, width_field=None, null=True, blank=True)
    user_f = models.ForeignKey(User,unique=True)
    #flat_f = models.ForeignKey(Flat,unique=True)
    #event_f = models.ForeignKey(Event,unique=True, null=True, blank=True) 
    #billing_f = models.ForeignKey(Billing,unique=True, null=True, blank=True)

    def __unicode__(self):
        return str(self.user_f) + ", " + str(self.dob)

