from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.template import RequestContext
from userena.decorators import secure_required
from guardian.decorators import permission_required_or_403
from userena.utils import signin_redirect, get_profile_model, get_user_model
from userena.forms import EditProfileForm
from accounts.forms import EditFreelancerProfileForm, EditOfferrerProfileForm
from django.views.generic import TemplateView
from userena import signals as userena_signals
from userena import settings as userena_settings
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from freelanceapp.models import SkillSet
from freelanceapp.skillset import create_base_skills
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

@secure_required
@permission_required_or_403('change_profile', (get_profile_model(), 'user__username', 'username'))
def profile_edit(requests, username, extra_context=None, **kwargs):
    user = get_object_or_404(get_user_model(),
                             username__iexact=username)

    profile = user.get_profile()

    if profile.profile_type == "freelancer":
        return redirect("/accounts/freelancer/%s/edit" %user.username)
    elif profile.profile_type == "offerrer":
        return redirect("/accounts/offerrer/%s/edit" %user.username)
    else:
        return redirect("/accounts/freelancer/%s/edit" %user.username)
        
    return redirect("/")	


@secure_required
@permission_required_or_403('change_profile', (get_profile_model(), 'user__username', 'username'))
def profile_edit_main(request, username, edit_profile_form=EditFreelancerProfileForm,
							template_name='userena/profile_form.html', success_url=None,
							extra_context=None, **kwargs):
    """
    Edit profile.

    Edits a profile selected by the supplied username. First checks
    permissions if the user is allowed to edit this profile, if denied will
    show a 404. When the profile is successfully edited will redirect to
    ``success_url``.

    :param username:
        Username of the user which profile should be edited.

    :param edit_profile_form:

        Form that is used to edit the profile. The :func:`EditProfileForm.save`
        method of this form will be called when the form
        :func:`EditProfileForm.is_valid`.  Defaults to :class:`EditProfileForm`
        from userena.

    :param template_name:
        String of the template that is used to render this view. Defaults to
        ``userena/edit_profile_form.html``.

    :param success_url:
        Named URL which will be passed on to a django ``reverse`` function after
        the form is successfully saved. Defaults to the ``userena_detail`` url.

    :param extra_context:
        Dictionary containing variables that are passed on to the
        ``template_name`` template.  ``form`` key will always be the form used
        to edit the profile, and the ``profile`` key is always the edited
        profile.

    **Context**

    ``form``
        Form that is used to alter the profile.

    ``profile``
        Instance of the ``Profile`` that is edited.

    """
    user = get_object_or_404(get_user_model(),
                             username__iexact=username)

    profile = user.get_profile()

    user_initial = {'first_name': user.first_name,
                    'last_name': user.last_name}

    form = edit_profile_form(instance=profile, initial=user_initial)

    if request.method == 'POST':
        form = edit_profile_form(request.POST, request.FILES, instance=profile,
                                 initial=user_initial)

        if form.is_valid():
            profile = form.save()
            skillset = request.POST.get('skillset')
            if skillset == None:
                pass
            elif skillset == "":
                profile.skills.clear()
            else:
                profile.skills.set(*skillset.lower().split(", "))
                result  = create_base_skills(skillset.split(", "))

            if userena_settings.USERENA_USE_MESSAGES:
                messages.success(request, _('Your profile has been updated.'),
                                 fail_silently=True)

            if success_url:
                # Send a signal that the profile has changed
                userena_signals.profile_change.send(sender=None,
                                                    user=user)
                redirect_to = success_url
            else: redirect_to = reverse('userena_profile_detail', kwargs={'username': username})
            return redirect(redirect_to)

    if not extra_context: extra_context = dict()
    extra_context['skills'] = json.dumps([ob.as_json() for ob in SkillSet.objects.all()])
    extra_context['form'] = form
    extra_context['profile'] = profile
    return ExtraContextTemplateView.as_view(template_name=template_name,
                                            extra_context=extra_context)(request)

