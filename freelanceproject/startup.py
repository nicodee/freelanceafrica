from django.conf import settings
from django.core.cache import cache
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import os

SITE_ID = settings.SITE_ID
DOMAIN_NAME = os.environ.get('DOMAIN_NAME')
DISPLAY_NAME = " ".join(os.environ.get('DISPLAY_NAME').split('_'))

def run():
    site = Site.objects.get(pk=1)
    site.domain = DOMAIN_NAME
    site.name = DISPLAY_NAME
    site.save()
    SITE_ID = site.id

    try:
        user = User.objects.get(username="admin")
        if user.is_superuser:
            pass
    except ObjectDoesNotExist, e:
        User.objects.create_superuser('admin', 'nnutsukpui@gmail.com', 'password')
        pass
