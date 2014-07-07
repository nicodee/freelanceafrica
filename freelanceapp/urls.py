from django.conf.urls import patterns, url
from freelanceapp import views
from freelanceapp.forms import ProjectForm

urlpatterns = patterns('',	
	url(r'^$', views.index, name='freelanceapp_home'),
	url(r'^job/$', views.job, name='freelanceapp_jobs'),
	url(r'^job/create$', views.create_job, {'project_form': ProjectForm}, name='freelanceapp_create_job' ),
	url(r'^about/$', views.about, name='freelanceapp_about'),
	url(r'^blog/$', views.blog, name='freelanceapp_blog'),
    url(r'^accounts/(?P<username>[\.\w-]+)/jobs/$', views.created_jobs, name="freelanceapp_created_jobs"),
    # View freelancer profiles
    url(r'^freelancers/page/(?P<page>[0-9]+)/$',
       views.FreelancerProfileListView.as_view(),
       name='freelanceapp_freelancers_list_paginated'),
    url(r'^freelancers/$',
       views.FreelancerProfileListView.as_view(),
       name='freelanceapp_freelancers_list'),
	)

handler500 = 'freelanceapp.views.custom_500'