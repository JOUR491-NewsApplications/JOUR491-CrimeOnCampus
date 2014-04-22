from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'reports.views.home', name='home'),
    url(r'^buildings/(?P<slug>[-\w]+)/$', 'reports.views.buildingdetail', name='buildingdetail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
