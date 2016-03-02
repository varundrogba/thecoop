from django.db import models
from aduser.models import AdUser

class Society(models.Model):
    soc_name = models.CharField(max_length=30)
    soc_address = models.CharField(max_length=50)
    soc_secretary = models.ForeignKey(AdUser,unique=True, related_name='Society_Secretary')
    soc_builder = models.ForeignKey(AdUser,unique=True, related_name='Society_Builder')
    #state_province = models.CharField(max_length=30)
    #country = models.CharField(max_length=50)
    #website = models.URLField()
    
    def __unicode__(self):
        return self.soc_name + ", " + self.soc_address


class Building(models.Model):
    bldg_name = models.CharField(max_length=30)
    #society = models.CharField(max_length=30)
    bldg_secretary = models.ForeignKey(AdUser,unique=True, related_name='Building_Secretary')
    no_of_flats = models.PositiveSmallIntegerField()
    #society = models.ForeignKey(Society,unique=True)
    properties = models.ManyToManyField(Society, related_name='Society_Properties')

    def __unicode__(self):
        return self.bldg_name

class Flat(models.Model):
    flat_owner = models.ForeignKey(AdUser,unique=True, related_name='Flat_Owner')
    flat_tenant = models.ForeignKey(AdUser,unique=True, related_name='Flat_Tenant')
    flat_no = models.PositiveSmallIntegerField()
    f_no_of_occupants = models.PositiveSmallIntegerField()
    f_sqft = models.PositiveSmallIntegerField()
    #bldg_f = models.ForeignKey(Building,unique=True)
    occupants = models.ManyToManyField(AdUser, related_name='Flat_Occupants')
    flats = models.ManyToManyField(Building, related_name='Flats')

    def __unicode__(self):
        return str(self.flat_no) + ", " + str(self.flat_owner) + ", " 
        #+ str(Building.bldg_name) - Ask Apoorv Later


    


