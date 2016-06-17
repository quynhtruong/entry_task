from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
	                    url(r'^list_all$', views.list_all, name='list_all')
						)