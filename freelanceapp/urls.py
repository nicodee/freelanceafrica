from django.conf.urls import patterns, url
from freelanceapp import views
from freelanceapp.forms import ProjectForm

urlpatterns = patterns('',	
	url(r'^$', views.index, name='freelanceapp_home'),
	url(r'^job/$', views.job, name='freelanceapp_jobs'),
	url(r'^job/create$', views.create_job, {'project_form': ProjectForm}, name='freelanceapp_create_job' ),
	url(r'^freelancer/$', views.freelancer, name='freelanceapp_freelancers'),
	url(r'^about/$', views.about, name='freelanceapp_about'),
	url(r'^blog/$', views.blog, name='freelanceapp_blog'),
    url(r'^accounts/(?P<username>[\.\w-]+)/jobs/$', views.created_jobs, name="freelanceapp_created_jobs"),
	)

handler500 = 'freelanceapp.views.custom_500'