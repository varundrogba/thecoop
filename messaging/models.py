from django.db import models
from event.models import event
from society.models import *
from billing.models import billing
from aduser.models import aduser

class Messages(models.Model):
    message = models.CharField(max_length=500)
    m_dtime = models.DateTimeField(auto_now=True, auto_now_add=True)
    message_origin= models.CharField(max_length=30)
