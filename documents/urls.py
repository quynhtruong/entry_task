from django.conf.urls import patterns, url

from documents import views

urlpatterns = patterns('',
	                    url(r'^get$', views.get, name='get',)
						)