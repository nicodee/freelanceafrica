from django.conf.urls import patterns, url
from freelanceapp import views
from freelanceapp.forms import ProjectForm

urlpatterns = patterns('',	
	url(r'^$', views.index, name='home'),
	url(r'^job/$', views.job, name='jobs'),
	url(r'^job/create$', views.create_job, {'project_form': ProjectForm}),
	url(r'^freelancer/$', views.freelancer, name='freelancers'),
	url(r'^about/$', views.about, name='about'),
	url(r'^blog/$', views.blog, name='blog'),
    url(r'^accounts/(?P<username>[\.\w-]+)/jobs/$', views.created_jobs, name="created-jobs"),
	)

handler500 = 'freelanceapp.views.custom_500'