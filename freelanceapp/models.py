from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext as _  
from accounts.models import MyProfile
from accounts import choices
import datetime
from django.utils.text import slugify
import uuid

class Project(models.Model):
	profile           = models.ForeignKey(MyProfile)
	name              = models.CharField(_('project name'), null=True, blank=True, max_length=50)
	short_description = models.TextField(_('short description'), max_length=300, blank=True)
	time_frame        = models.IntegerField(_('duration'), blank=True, default=30)
	time_frame_unit   = models.CharField(_('duration units'), choices=choices.BIDDING_TIME_FRAME_CHOICES, max_length=50, blank=True,)
	bidding_deadline  = models.DateTimeField(default=datetime.date.today())
	bidding_startdate = models.DateTimeField(default=datetime.date.today())
	budget_currency   = models.CharField(_('project budget currency'), null=True, blank=True, max_length=50, default='$')
	budget            = models.CharField(_('project budget'), null=True, blank=True, max_length=50)  
	created           = models.DateTimeField(auto_now_add=True, default=datetime.date.today())
	slug              = models.SlugField(max_length=255, default=datetime.date.today())
	skills            = TaggableManager()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(unicode(str(uuid.uuid4()), 'utf-8'))
		super(Project, self).save(*args, **kwargs)



# class Skill(models.Model):
	# pass

class SkillSet(models.Model):
	value = models.CharField(_('skill'), unique=True, max_length=50, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True, default=datetime.date.today())

	class Meta:
		ordering = ["value"]

	def titled(self):
		"Returns skill in upper case format eg. 'web developer' becomes 'WEB DEVELOPER'"
		return self.value.upper()

	def as_json(self):
		return dict(value=self.titled())
