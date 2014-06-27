from django.conf import settings
from django.core.cache import cache
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

SITE_ID = settings.SITE_ID

def run():
    site = Site.objects.get(pk=1)
    site.domain = 'localhost:8000'
    site.name = 'Freelance Africa Development'
    site.save()
    SITE_ID = site.id

    try:
        user = User.objects.get(username="admin")
        if user.is_superuser:
            pass
    except ObjectDoesNotExist, e:
        User.objects.create_superuser('admin', 'nnutsukpui@gmail.com', 'password')
        pass

def online_site(request):
    site_url = request.get_host()
    
    if("freelanceafrica.herokuapp.com" in site_url):
        online_site = Site.objects.get(pk=1)
        online_site.domain = "freelanceafrica.herokuapp.com"
        online_site.name = "Freelance Africa"
        online_site.save()
        SITE_ID = online_site.id

    elif("freelanceafrica-test.herokuapp.com" in site_url):
        online_site = Site.objects.get(pk=1)
        online_site.domain = "freelanceafrica-test.herokuapp.com"
        online_site.name = "Freelance Africa Test"
        online_site.save()
        SITE_ID = online_site.id
