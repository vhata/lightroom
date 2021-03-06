from django.conf.urls import patterns, include, url
from lights import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lightroom.views.home', name='home'),
    # url(r'^lightroom/', include('lightroom.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^get/(?P<pos_x>\d+)/(?P<pos_y>\d+)/$', views.get, name='get'),
    url(r'^get_multi$', views.get_multi, name='get_multi'),
    url(r'^set/(?P<pos_x>\d+)/(?P<pos_y>\d+)/(?P<intensity>\d+)/$', views.set, name='set'),
    url(r'^toggle/(?P<pos_x>\d+)/(?P<pos_y>\d+)/$', views.toggle, name='toggle'),
    url(r'^set_multi$', views.set_multi, name='set_multi'),
    url(r'^set_js$', views.set_js, name='set_js'),
    url(r'^reset(?:/(?P<size_x>\d+)(?:/(?P<size_y>\d+))?)?/$', views.reset, name='reset'),

    url(r'resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/resources'}),
)
