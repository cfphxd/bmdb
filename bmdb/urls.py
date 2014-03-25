from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bmdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    ## Section ADMIN ##
    url(r'^admin/', include(admin.site.urls)),

    # API url. parameter 1 is report and 2 is a parameter depending on the report. E.g. search term for search functionality
    url(r'^api/(\w{0,50})/(\w{0,50})/(\w{0,50})/','api.views.report_view'),

    ## Section HOME ##
    url(r'^/home/','web.views.page_home'),

    ## Section FOOD CLAIMS ##
    url(r'^food-claims/$','web.views.page_food_claims'),
    url(r'^updates/$','web.views.page_fc_updates'),
    url(r'^nz---australia-information/$','web.views.page_fc_nz_info'),
    url(r'^world-wide-information/$','web.views.page_fc_world_info'),
    url(r'^food-comp-db/$','web.views.page_fc_food_composition_db'),
    url(r'^making-a-claim/$','web.views.page_fc_make_claim'),

    ## Section DATABASE ##
    url(r'^database/$','web.views.page_database'),
    url(r'^search/$','web.views.page_db_search'),
    url(r'^register/$','web.views.page_db_register'),
    url(r'^faqs/$','web.views.page_db_faq'),

    ## Section ABOUT ##
    url(r'^about/$','web.views.page_about'),
    url(r'^contact/$','web.views.page_ab_contact_us'),
    url(r'^terms---conditions/$','web.views.page_ab_terms'),

    ## Section DATA INPUT ##
    url(r'^data-input$','adm.views.sequencial_data_input'),
)
