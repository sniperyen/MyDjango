from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^setlang/$', 'django.views.i18n.set_language', name='setlang'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^timer/', include('timer.urls')),
)
