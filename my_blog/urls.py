from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^my_blog/', include('my_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gb_home.views.home', name='home'),
    url(r'^blog/$', 'blog.views.index', name='blog_archive'),
    url(r'^blog/(?P<slug>[\w\-]+)/$', 'blog.views.post', name='view_post'),
    url(r'^contact/$', 'gb_home.views.contact', name='contact'),
    url(r'^social/$', 'gb_home.views.social', name='social'),
    # Trying to get pdfs to work
    # url(r'^pdf/(?P<filename>[a-z0-9A-Z_\-]*\.pdf)$', 'gb_home.views.pdf', name='my_pdf'),



)
