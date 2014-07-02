from django.conf.urls import patterns, url
from freelanceapp import views

urlpatterns = patterns('',	
	url(r'^$', views.index, name='home'),
	url(r'^job/$', views.job, name='jobs'),
	url(r'^job/create$', views.create_job, name='new job'),
	url(r'^freelancer/$', views.freelancer, name='freelancers'),
	url(r'^about/$', views.about, name='about'),
	url(r'^blog/$', views.blog, name='blog'),
)

handler500 = 'freelanceapp.views.custom_500'