from django.db import models

class Society(models.Model):
    soc_name = models.CharField(max_length=30)
    soc_address = models.CharField(max_length=50)
    soc_owner = models.CharField(max_length=60)
    soc_builder = models.CharField(max_length=60)
    #state_province = models.CharField(max_length=30)
    #country = models.CharField(max_length=50)
    #website = models.URLField()


class Building(models.Model):
    bldg_name = models.CharField(max_length=30)
    society = models.CharField(max_length=30)
    bldg_owner = models.CharField(max_length=30)
    no_of_flats = models.PositiveSmallIntegerField(9999)
    soc_f = models.ForeignKey(Society,unique=True)

class Flat(models.Model):
    flat_owner = models.CharField(max_length=30)
    flat_tenant = models.CharField(max_length=30)
    flat_no = models.PositiveSmallIntegerField(9999)
    f_no_of_occupants=models.PositiveSmallIntegerField(9999)
    f_sqft = models.PositiveSmallIntegerField(9999)
    bldg_f = models.ForeignKey(Building,unique=True)
    


