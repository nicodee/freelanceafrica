from django.conf.urls import patterns, include, url

from django.contrib import admin
from accounts.forms import (SignupFormOnlyEmailExtra, AuthenticationFormExtra, 
                            ChangeEmailFormExtra, EditProfileFormExtra, 
                            PasswordChangeFormExtra, PasswordResetFormExtra)
from django.conf import settings
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freelanceproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('freelanceapp.urls')),
    url(r'^$', include('freelanceapp.urls')),
    url(r'^signup/$', 'userena.views.signup', {'signup_form': SignupFormOnlyEmailExtra}),
    url(r'^signin/$', 'userena.views.signin', {'auth_form': AuthenticationFormExtra}),
    url(r'^accounts/signup/$', 'userena.views.signup', {'signup_form': SignupFormOnlyEmailExtra}),
    url(r'^accounts/signin/$', 'userena.views.signin', {'auth_form': AuthenticationFormExtra}),
    url(r'^signout/$', 'userena.views.signout'),
    url(r'^accounts/(?P<username>[\.\w-]+)/email/$', 'userena.views.email_change', {'email_form': ChangeEmailFormExtra}),
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$', 'userena.views.profile_edit', {'edit_profile_form' : EditProfileFormExtra}),
    url(r'^accounts/(?P<username>[\.\w-]+)/password/$', 'userena.views.password_change', {'pass_form' : PasswordChangeFormExtra}),
    url(r'^accounts/password/reset/$', auth_views.password_reset, {'password_reset_form' : PasswordResetFormExtra}),
    url(r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))