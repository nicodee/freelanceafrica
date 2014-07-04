from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from accounts import choices
from freelanceapp.models import Project

class ProjectForm(ModelForm):
	def __init__(self, *args, **kwargs):
	    super(ProjectForm, self).__init__(*args, **kwargs)
	    self.fields['name'].widget.attrs['class'] = 'form-control input required'
	    self.fields['short_description'].widget.attrs['class'] = 'form-control input required'
	    self.fields['time_frame'].widget.attrs['class'] = 'form-control input required'
	    self.fields['time_frame_unit'].widget.attrs['class'] = 'form-control input required'
	    self.fields['bidding_deadline'].widget.attrs['class'] = 'form-control input required'
	    self.fields['bidding_startdate'].widget.attrs['class'] = 'form-control input required'
	    # self.fields['budget_currency'].widget.attrs['class'] = 'form-control input required'
	    self.fields['budget'].widget.attrs['class'] = 'form-control input required'
        # self.fields.insert(0,'mugshot', self.fields['mugshot'])
        # self.fields.insert(1,'identification', self.fields['identification'])

	class Meta:
		model = Project
		fields = ['name', 'short_description', 'time_frame', 'time_frame_unit', 'bidding_deadline', 'bidding_startdate', 'budget_currency', 'budget']
		exclude = ['profile','created', 'budget_currency', 'slug']
		# error_messages = {
		# 	'name': {'required': _("Please enter your project's name.")},
		# 	'tag_line': {'required': _("A tagline is required for your project.")},
		# 	'goal': {'required': _("A valid amount is required.")},
		# 	'image': {'required': _("Please upload an image for your project")},
		# 	'city': {'required': _("Please the city of your project")},
		# 	'duration': {'required': _("The project should not exceed 60 days")}
		# 	}
		# 	
		labels = {
            'name': _('Title'),
			'short_description': _('Describe the project in a few words'),
			'time_frame': _('Duration of project'),
			'bidding_deadline': _('When should bidding for your project start?'),
			'bidding_startdate': _('When should bidding for your project end?'),
			'budget': _('How much are you willing to pay')
        }
		widgets = {			
			'name': forms.TextInput(attrs={'type': 'text', 'id': 'id_name', 'placeholder': 'name', 'required': 'true'}),
			'short_description': forms.Textarea(attrs={'type': 'text', 'id': 'id_short_description', 'maxlength':'300','placeholder': 'What is does the project entail?', 'cols': '30', 'rows': '5','style': 'resize: vertical','required': 'true'}),
			'time_frame': forms.TextInput(attrs={'type': 'number', 'id': 'id_time_frame', 'placeholder': 'How long will it take', 'required': 'true'}),
			'bidding_deadline': forms.TextInput(attrs={'type': 'date',  'id': 'id_bidding_deadline', 'placeholder': 'yyyy-mm-dd', 'required': 'true'}),
			'bidding_startdate': forms.TextInput(attrs={'type': 'date', 'id': 'id_bidding_startdate', 'placeholder': 'yyyy-mm-dd', 'required': 'true'}),
			'budget': forms.TextInput(attrs={'type': 'number', 'min':'1', 'step':'1', 'id': 'id_budget', 'placeholder': '', 'required': 'true'})
        }


              
 
        
  
 
   
            