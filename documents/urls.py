from django.conf.urls import patterns, url

from documents import views

urlpatterns = patterns('',
	                    url(r'^upload_file$', views.upload_file, name='upload_file',)
						)