from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

def index(request, template="freelanceapp/index.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)
