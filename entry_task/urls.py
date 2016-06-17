from django.conf.urls import patterns, include, url
from django.contrib import admin

import events.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'entry_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^transaction/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
