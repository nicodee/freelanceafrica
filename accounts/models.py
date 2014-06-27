from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile
import datetime

class MyProfile(UserenaBaseProfile):  
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
        (3, _('None')),
    )

    PROFILE_TYPE = (
    	('freelancer', _('FREELANCER')),
        ('offerrer', _('OFFERRER')),
    )
    
    gender               = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, default=3)
    birth_date           = models.DateField(_('birth date'), null=True, blank=True, default=datetime.date(1990,1,1))
    bio                  = models.TextField(_('short bio'), max_length=250, blank=True)
    country_of_origin    = models.CharField(_('country of origin'), max_length=50, blank=True)
    country_of_residence = models.CharField(_('country of residence'), max_length=50, blank=True)
    user                 = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
    location             = models.CharField(_('location'), max_length=50, blank=True)
    phone                = models.CharField(_('phone'), max_length=20, blank=True)
    profile_type         = models.CharField(_('profile type'), max_length='20', choices=PROFILE_TYPE, default=1)
    created              = models.DateTimeField(auto_now_add=True, default=datetime.date.today())
    industry             = models.CharField(_('industry'), max_length=50, blank=True)
    company              = models.CharField(_('company'), max_length=50, blank=True)      