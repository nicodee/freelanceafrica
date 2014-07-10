from django.conf.urls import patterns, include, url

from django.contrib import admin
from accounts.forms import (SignupFormOnlyEmailExtra, AuthenticationFormExtra, 
                            ChangeEmailFormExtra, EditFreelancerProfileForm,
                            EditOfferrerProfileForm, PasswordChangeFormExtra, PasswordResetFormExtra)
from django.conf import settings
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
admin.autodiscover()
from userena import settings as userena_settings
from userena.compat import auth_views_compat_quirks

def merged_dict(dict_a, dict_b):
    """Merges two dicts and returns output. It's purpose is to ease use of
    ``auth_views_compat_quirks``
    """
    dict_a.update(dict_b)
    return dict_a

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freelanceproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('freelanceapp.urls')),
    url(r'^$', include('freelanceapp.urls')),
    url(r'^signup/$', 'userena.views.signup', {'signup_form': SignupFormOnlyEmailExtra}, name='accounts_signup'),
    url(r'^signin/$', 'userena.views.signin', {'auth_form': AuthenticationFormExtra}, name='accounts_signin'),
    url(r'^account/$', accounts_views.user_authentication, {'auth_form': AuthenticationFormExtra, 'signup_form': SignupFormOnlyEmailExtra}, name='accounts_user_authentication'),
    url(r'^accounts/signup/$', 'userena.views.signup', {'signup_form': SignupFormOnlyEmailExtra}),
    url(r'^accounts/signin/$', 'userena.views.signin', {'auth_form': AuthenticationFormExtra}),
    url(r'^signout/$', 'userena.views.signout'),
    url(r'^accounts/(?P<username>[\.\w-]+)/email/$', 'userena.views.email_change', {'email_form': ChangeEmailFormExtra}),
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$', accounts_views.profile_edit, name="accounts_profile_edit"),
    url(r'^accounts/(?P<username>[\.\w-]+)/password/$', 'userena.views.password_change', {'pass_form' : PasswordChangeFormExtra}),
    url(r'^accounts/password/reset/$',
       auth_views.password_reset,
       merged_dict({'template_name': 'userena/password_reset_form.html',
                    'email_template_name': 'userena/emails/password_reset_message.txt',
                    'password_reset_form' : PasswordResetFormExtra,
                    'extra_context': {'without_usernames': userena_settings.USERENA_WITHOUT_USERNAMES}
                   }, auth_views_compat_quirks['userena_password_reset']),
       name='userena_password_reset'),
    # Edit profile
    url(r'^accounts/offerrer/(?P<username>[\.\w-]+)/edit/$', accounts_views.profile_edit_main, {'edit_profile_form' : EditOfferrerProfileForm}, name='accounts_offerrer_edit'),
    url(r'^accounts/freelancer/(?P<username>[\.\w-]+)/edit/$', accounts_views.profile_edit_main, {'edit_profile_form' : EditFreelancerProfileForm}, name='accounts_freelancer_edit'),
    
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', accounts_views.activate, name='accounts_activate'),

    url(r'^accounts/', include('userena.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))