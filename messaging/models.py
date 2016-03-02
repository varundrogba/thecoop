from django.db import models
from aduser.models import AdUser

class Messages(models.Model):
    message = models.CharField(max_length=500)
    m_dtime = models.DateTimeField(auto_now=True, auto_now_add=True)
    message_creator = models.ForeignKey(AdUser,unique=True,related_name='Message_Creator')
    message_owners = models.ManyToManyField(AdUser,related_name='Message_Viewers')

    def __unicode__(self):
    	return str(self.m_dtime) + ", "  + str(self.message_creator)