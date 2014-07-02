from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

def index(request, template="freelanceapp/index.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)

def job(request, template="freelanceapp/job/job.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)

def freelancer(request, template="freelanceapp/freelancer.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)

def about(request, template="freelanceapp/about.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)

def blog(request, template="freelanceapp/blog.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)

def create_job(request, template="freelanceapp/job/create_job.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)


