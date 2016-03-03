from django.conf.urls import patterns, include, url
from thecoop.views import cooplog,test
from django.contrib import admin

from society.api import SocietyResource

society_resource = SocietyResource()

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thecoop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', cooplog),
    url(r'^test/',test),
    url(r'^api/', include(society_resource.urls)),
    #url(r'^loginp/', cooplog),
)
