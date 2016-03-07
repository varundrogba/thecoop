from tastypie.resources import ModelResource,ALL, ALL_WITH_RELATIONS
from aduser.models import AdUser
from tastypie.authorization import Authorization

class AdUserResource(ModelResource):
    class Meta:
        queryset = AdUser.objects.all()
        resource_name = 'aduser'
 
