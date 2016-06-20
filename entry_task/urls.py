from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'entry_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    url(r'^channels/', include('channels.urls')),
)
