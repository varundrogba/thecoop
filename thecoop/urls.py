from django.conf.urls import patterns, include, url
from thecoop.views import cooplogin, cooplog
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thecoop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', cooplogin),
    url(r'^loginp/', cooplog),
)
