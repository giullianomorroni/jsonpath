from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

handler404 = 'artigos.views._404'
handler500 = 'artigos.views._500'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jpath.views.home', name='home'),
    url(r'^query/', 'jpath.views.query', name='query'),
    url(r'^how_to/en', 'jpath.views.how_to_en', name='how_to_en'),
    url(r'^how_to/pt', 'jpath.views.how_to_pt', name='how_to_pt'),
    # url(r'^jpath/', include('jpath.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
