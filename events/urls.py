from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
	                    url(r'^list$', views.list_all, name='list',)
						)