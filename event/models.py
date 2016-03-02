from django.db import models
from aduser.models import AdUser

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
    event_owner = models.ManyToManyField(AdUser, related_name='Event_Viewers')
    event_creator = models.ForeignKey(AdUser,unique=True, related_name='Event_Creator')
    event_type = models.CharField(max_length=1, choices = event_CHOICES)
    event_dtime = models.DateTimeField(auto_now=True, auto_now_add=True)


    def __unicode__(self):
        return str(self.event_name) + ", " + str(self.event_owner) + ", " + str(self.event_dtime)

