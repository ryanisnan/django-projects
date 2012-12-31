from django.conf.urls.defaults import patterns, url
from projects import views

urlpatterns = patterns('',
	url(r'^$', views.projects_index, name='projects_index'),
	url(r'^(?P<slug>[a-z0-9\-\.]+)/$', views.project_detail, name='project_detail'),
)