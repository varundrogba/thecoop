from tastypie.resources import ModelResource
from messaging.models import Messages

class MessagingResource(ModelResource):
    class Meta:
        queryset = Messages.objects.all()
        resource_name = 'messaging'
