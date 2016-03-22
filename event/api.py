from tastypie.resources import ModelResource
from event.models import Event


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'



'''
    def prepend_urls(self):
    return [
        url(r"^(?P<resource_name>%s)/user/?P<user_id>%s), self.wrap_view('fetch_username'), name="api_fetchusername"),
        ]	

'''