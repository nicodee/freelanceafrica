from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile
from userena import settings as userena_settings
from userena.utils import get_gravatar
from freelanceproject import choices
import datetime
import os
from PIL import Image
from django.core.files.storage import default_storage as storage
from django.core.validators import MaxValueValidator

def get_image_path(instance, filename):
    return os.path.join('mugshots/identification/%s/'%(instance.user.username), filename)

class MyProfile(UserenaBaseProfile):
    gender                     = models.PositiveSmallIntegerField(_('gender'), choices=choices.GENDER_CHOICES, blank=True, default=3)
    birth_date                 = models.DateField(_('birth date'), null=True, blank=True, default=datetime.date(1990,1,1))
    country_of_origin          = models.CharField(_('country of origin'), max_length='50', choices=choices.AFRICAN_COUNTRIES)
    country_of_residence       = models.CharField(_('country of residence'), max_length='50', choices=choices.AFRICAN_COUNTRIES)
    user                       = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
    location                   = models.CharField(_('location'), max_length=50, blank=True)
    phone                      = models.CharField(_('phone'), max_length=20, blank=True)
    profile_type               = models.CharField(_('profile type'), max_length='20', choices=choices.PROFILE_TYPE, default=1)
    created                    = models.DateTimeField(auto_now_add=True, default=datetime.date.today())
    identification             = models.ImageField(max_length=500, upload_to=get_image_path, blank=True, null=True)      
    bio                        = models.TextField(_('short bio'), max_length=250, blank=True)
    drive                      = models.TextField(_('personal drive'), max_length=20, blank=True)
    industry                   = models.CharField(_('industry'), max_length=50, blank=True)
    company                    = models.CharField(_('company'), max_length=50, blank=True)
    
    __original_identiification = None

    def __init__(self, *args, **kwargs):
        super(MyProfile, self).__init__(*args, **kwargs)
        self.__original_identification = self.identification

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.identification != self.__original_identification:
            self.compress_image()
        super(MyProfile, self).save(*args, **kwargs)
        if not self.identification:
            return
        elif self.identification != self.__original_identification:
            self.compress_image()

    def compress_image(self):
        file_path = self.identification.name
        filename_base, filename_ext = os.path.splitext(file_path)
        thumb_file_path = filename_base + filename_ext
        try:
            # resize the original image and return url path of the thumbnail
            f = storage.open(file_path, 'r')
            image = Image.open(f)
            format = image.format
            width, height = image.size

            width = int(width * 0.6)
            height = int(height * 0.6)   
            size = (width, height)
            image = image.resize(size, Image.ANTIALIAS)

            f_thumb = storage.open(thumb_file_path, "w")
            image.save(f_thumb, format, quality=80)
            f_thumb.close()
            return "success"
        except:
            return "error"

    def get_id_url(self):
        """
        Returns the image containing the identification for the user.

        The identification can be a uploaded image or a Gravatar.

        Gravatar functionality will only be used when
        ``USERENA_MUGSHOT_GRAVATAR`` is set to ``True``.

        :return:
            ``None`` when Gravatar is not used and no default image is supplied
            by ``USERENA_MUGSHOT_DEFAULT``.

        """
        # First check for a identification and if any return that.
        if self.identification:
            return self.identification.url

        # Use Gravatar if the user wants to.
        if userena_settings.USERENA_MUGSHOT_GRAVATAR:
            return get_gravatar(self.user.email,
                                userena_settings.USERENA_MUGSHOT_SIZE,
                                userena_settings.USERENA_MUGSHOT_DEFAULT)

        # Gravatar not used, check for a default image.
        else:
            if userena_settings.USERENA_MUGSHOT_DEFAULT not in ['404', 'mm',
                                                                'identicon',
                                                                'monsterid',
                                                                'wavatar']:
                return userena_settings.USERENA_MUGSHOT_DEFAULT
            else:
                return None

# class OfferrerProfile(MyProfile):
#     profile  = models.OneToOneField(MyProfile, unique=True,verbose_name=_('user'), related_name='offerrer_profile')
    
# class FreelancerProfile(MyProfile):
#     profile = models.OneToOneField(MyProfile, related_name='freelancer_profile')

# class FreelancerSkills(models.Model):
#     profile = models.ForeignKey(FreelancerProfile)
#     title   = models.CharField(_('skill'), max_length=50, blank=True)


