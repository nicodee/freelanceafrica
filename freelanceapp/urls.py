from django.conf.urls import patterns, url
from freelanceapp import views

urlpatterns = patterns('',	
	url(r'^$', views.index, name='home'),
)

handler500 = 'freelanceapp.views.custom_500'