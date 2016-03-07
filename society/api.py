from tastypie.resources import ModelResource
from society.models import Society,Building,Flat


class SocietyResource(ModelResource):
    class Meta:
        queryset = Society.objects.all()
        resource_name = 'society'

class BuildingResource(ModelResource):
    class Meta:
        queryset = Building.objects.all()
        resource_name = 'building'

class FlatResource(ModelResource):
    class Meta:
        queryset = Flat.objects.all()
        resource_name = 'flat'
