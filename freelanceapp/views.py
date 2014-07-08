from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from freelanceapp.forms import ProjectForm
from freelanceapp.models import Project, SkillSet
from django.contrib.auth.decorators import login_required
from userena.decorators import secure_required
from guardian.decorators import permission_required_or_403
from userena.utils import signin_redirect, get_profile_model, get_user_model
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from freelanceapp.skillset import create_base_skills
from userena import settings as userena_settings
import json

class ExtraContextTemplateView(TemplateView):
    """ Add extra context to a simple template view """
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context

    # this view is used in POST requests, e.g. signup when the form is not valid
    post = TemplateView.get

class FreelancerProfileListView(ListView):
    """ Lists all freelancer profiles """
    context_object_name='profile_list'
    page=1
    paginate_by=50
    template_name="freelanceapp/freelancer.html"
    extra_context=None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FreelancerProfileListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get('page', None))
        except (TypeError, ValueError):
            page = self.page

        if userena_settings.USERENA_DISABLE_PROFILE_LIST \
           and not self.request.user.is_staff:
            raise Http404

        if not self.extra_context: self.extra_context = dict()

        context['page'] = page
        context['paginate_by'] = self.paginate_by
        context['extra_context'] = self.extra_context

        return context

    def get_queryset(self):
        profile_model = get_profile_model()
        queryset = profile_model.objects.get_visible_profiles(self.request.user).select_related().filter(profile_type="freelancer")
        return queryset

class ProjectListView(ListView):
    """ Lists all projects """
    context_object_name='project_list'
    page=1
    paginate_by=5
    template_name="freelanceapp/job/job.html"
    extra_context=None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectListView, self).get_context_data(**kwargs)
        try:
            page = int(self.request.GET.get('page', None))
        except (TypeError, ValueError):
            page = self.page

        if not self.extra_context: self.extra_context = dict()

        context['page'] = page
        context['paginate_by'] = self.paginate_by
        context['extra_context'] = self.extra_context

        return context

    def get_queryset(self):
        projects = Project.objects.all()
        queryset = projects
        return queryset

def index(request, template="freelanceapp/index.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)

# def job(request, template="freelanceapp/job/job.html", context=None):
# 	if request.user.is_authenticated:
# 		context = {'user':request.user}
# 	return render_to_response(template, context)

# def freelancer(request, template="freelanceapp/freelancer.html", context=None):
# 	if request.user.is_authenticated:
# 		context = {'user':request.user}
# 	return render_to_response(template, context)


def about(request, template="freelanceapp/about.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)

def blog(request, template="freelanceapp/blog.html", context=None):
	if request.user.is_authenticated:
		context = {'user':request.user}
	return render_to_response(template, context)


@login_required
def create_job(request, template_name="freelanceapp/job/create_job.html", project_form=ProjectForm, extra_context=None, **kwargs):
	if request.user.is_authenticated:
		profile = request.user.get_profile()
		form = project_form()
		if request.method == 'POST':
			form = project_form(request.POST)

			if form.is_valid():
				def project_exists():
					return Project.objects.filter(profile=profile, name=request.POST.get('name')).exists()
					
				if not project_exists():
					new_project = Project(profile=profile,
										name=request.POST.get('name'),
										short_description=request.POST.get('short_description'),
										time_frame=request.POST.get('time_frame'),
										time_frame_unit=request.POST.get('time_frame_unit'),
										bidding_deadline=request.POST.get('bidding_deadline'),
										bidding_startdate=request.POST.get('bidding_startdate'),
										budget=request.POST.get('budget')
										)
					new_project.save()
					new_project.skills.add(*request.POST.get('skills').lower().split(", "))
					result  = create_base_skills(request.POST.get('skills').split(", "))
					return redirect("/accounts/%s/jobs" %(request.user.username))

		if not extra_context: extra_context = dict()
		extra_context['skills'] = json.dumps([ob.as_json() for ob in SkillSet.objects.all()])
		extra_context['form'] = form
		extra_context['profile'] = profile

	return ExtraContextTemplateView.as_view(template_name=template_name,
                                            extra_context=extra_context)(request)

@secure_required
def created_jobs(request, username, template_name="freelanceapp/created_jobs.html", extra_context=None, **kwargs):
	user    = get_object_or_404(get_user_model(), username__iexact=username)
	profile = user.get_profile()

	if user == request.user:
		profile      = user.get_profile()
		created_jobs = Project.objects.filter(profile=profile)

		if not extra_context: extra_context = dict()
		extra_context['user']      = request.user
		extra_context['profile']      = profile
		extra_context['created_jobs'] = created_jobs
		return render_to_response(template_name,extra_context)

	return redirect("/")
