from django.db import models
from aduser.models import AdUser

Society = 'S'
Personal = 'P'
bill_CHOICES = (
(Society, 'Society'),
(Personal, 'Personal'),
)

class Billing(models.Model):
    bill_name = models.CharField(max_length=60)
    bill_type = models.CharField(max_length=1, choices = bill_CHOICES)
    bill_amtpaid = models.PositiveSmallIntegerField()
    bill_amtpending = models.PositiveSmallIntegerField()
    bill_totalamt = models.PositiveSmallIntegerField()
    bill_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
    bill_creator = models.ForeignKey(AdUser,unique=True, related_name='Bill_Creator')
    bill_owner = models.ManyToManyField(AdUser, related_name='Bill_Debtors')
    
    def __unicode__(self):
        return str(self.bill_name) + ", " + str(self.bill_datetime)


        #BILL_CREATOR=UNIQUE?? - IS IT REQUIRED?
    
