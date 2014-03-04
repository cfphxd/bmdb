from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bmdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # API url. parameter 1 is report and 2 is a parameter depending on the report. E.g. search term for search functionality
    url(r'^api/(\w{0,50})/(\w{0,50})/(\w{0,50})/','api.views.report_view'),
    url(r'^search/$','web.views.load_page_search'),
)
