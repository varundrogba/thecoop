from tastypie.resources import ModelResource,ALL, ALL_WITH_RELATIONS
from aduser.models import AdUser
from tastypie.authorization import Authorization

class AdUserResource(ModelResource):
    class Meta:
        queryset = AdUser.objects.all()
        resource_name = 'aduser'
 

	def user_detail(request, username):
		res = AdUserResource()
		request_bundle = res.build_bundle(request=request)
		user = res.obj_get(request_bundle, username=username)