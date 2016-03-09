from django.conf.urls import patterns, include, url
from thecoop.views import cooplog,test,cooplogsuc
from django.contrib import admin
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie import *

from society.api import SocietyResource
from society.api import BuildingResource
from society.api import FlatResource
from messaging.api import MessagingResource
from billing.api import BillingResource
from event.api import EventResource
from aduser.api import AdUserResource


society_resource = SocietyResource()
building_resource = BuildingResource()
flat_resource = FlatResource()
event_resource = EventResource()
billing_resource = BillingResource()
aduser_resource = AdUserResource()
messaging_resource = MessagingResource()



thecoop_api = Api(api_name='thecoop_api')

thecoop_api.register(SocietyResource())
thecoop_api.register(BuildingResource())
thecoop_api.register(FlatResource())
thecoop_api.register(EventResource())
thecoop_api.register(BillingResource())
thecoop_api.register(AdUserResource())
thecoop_api.register(MessagingResource())



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thecoop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', cooplog),
    url(r'^logsuc/', cooplogsuc),
    url(r'^test/',test),
    url(r'^api/', include(thecoop_api.urls)),
    #url(r'^api/', include(society_resource.urls)),
    #url(r'^loginp/', cooplog),
)
