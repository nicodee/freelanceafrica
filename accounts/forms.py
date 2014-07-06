from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from userena.forms import SignupFormTos, AuthenticationForm, ChangeEmailForm, EditProfileForm, SignupFormOnlyEmail
from userena.utils import get_profile_model
from accounts import choices
USERNAME_RE = r'^[\.\w]+$'


class SignupFormOnlyEmailExtra(SignupFormOnlyEmail):
    """
    Adding extra first and last name fields to the signup form.

    """
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required', 'placeholder':'Email', 'name':'email', 'type':'email',  'required':'true',  'id':'id_email'})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)), label=_("Email"))

    attrs_dict = ({'class':'form-control required', 'placeholder':'Password', 'name':'password1', 'type':'password', 'id':'id_password1'})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label=_("Create password"))

    attrs_dict = ({'class':'form-control required', 'placeholder':'Confirm password', 'name':'password2', 'type':'password', 'id':'id_password2'})
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label=_("Repeat password"))

    def save(self, *args, **kwargs):
        new_user = super(SignupFormOnlyEmailExtra, self).save(*args, **kwargs)
        return new_user


class AuthenticationFormExtra(AuthenticationForm):
    """
    Styling AuthenticationForm with bootstrap.
    """
    attrs_dict = {}
    attrs_dict = ({'class':'form-control required', 'placeholder':'Password', 'name':'password', 'type':'password', 'id':'id_password'})
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label=_("Password"))


class ChangeEmailFormExtra(ChangeEmailForm):
    """
    Styling ChangeEmailForm with bootstrap.
    """
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required', 'placeholder':'Email', 'name':'email', 'type':'email',  'required':'true',  'id':'id_email'})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)), label=_("New Email")) 


class PasswordChangeFormExtra(PasswordChangeForm):

    error_messages = dict(PasswordChangeForm.error_messages)
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required', 'placeholder':'Old Password', 'name':'old_password', 'type':'password', 'id':'old_password'})
    old_password = forms.CharField(label=_(u'Old Password'), widget=forms.PasswordInput(attrs=attrs_dict))
    
    attrs_dict = ({'class':'form-control required', 'placeholder':'New Password', 'name':'new_password1', 'type':'password', 'id':'id_new_password1'})
    new_password1 = forms.CharField(label=_(u'New Password'), widget=forms.PasswordInput(attrs=attrs_dict))
    

    attrs_dict = ({'class':'form-control required', 'placeholder':'Confirm New password', 'name':'new_password2', 'type':'password', 'id':'id_new_password2'})
    new_password2 = forms.CharField(label=_(u'Confirm New Password'), widget=forms.PasswordInput(attrs=attrs_dict))

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user


class PasswordResetFormExtra(PasswordResetForm):
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required', 'placeholder':'Email', 'name':'email', 'type':'email',  'required':'true',  'id':'id_email'})
    email = forms.EmailField(label=_(u'Email'), widget=forms.TextInput(attrs=attrs_dict))


class EditOfferrerProfileForm(EditProfileForm):
    attrs_dict = {}

    mugshot = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'id_mugshot'}), required=False)

    identification = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'id_identification'}), required=False)

    attrs_dict = ({'class':'form-control required', 'placeholder':'First Name','name':'first_name','type':'text','id':'id_first_name','required':'true'})
    first_name = forms.CharField(label=_(u'First name'), max_length=30, widget=forms.TextInput(attrs=attrs_dict), required=True)

    attrs_dict = ({'class':'form-control required', 'placeholder':'Last Name', 'name':'last_name', 'type':'text', 'id':'id_last_name', 'required':'true'})
    last_name = forms.CharField(label=_(u'Last name'), max_length=30, widget=forms.TextInput(attrs=attrs_dict), required=True)
    
    attrs_dict = ({  'class': 'form-control required', 'name': 'gender' })
    gender = forms.ChoiceField(label=_(u'Gender'),choices=choices.GENDER_CHOICES, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'date', 'class': 'form-control', 'name': 'birth_date'})
    birth_date = forms.DateField(label=_(u'Birth Date'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({  'class': 'form-control required', 'name': 'profile_type' })
    profile_type = forms.ChoiceField(label=_(u'I am here as a'), choices=choices.PROFILE_TYPE, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'location' })
    location = forms.CharField(label=_(u'Location'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({'class': 'form-control', 'cols': '30', 'rows': '5', 'name': 'bio', 'style': 'resize: vertical', 'maxlength':'250'})
    bio = forms.CharField(label=_(u'Short awesome self-description (max. 250 characters)'), max_length=250, widget=forms.Textarea(attrs=attrs_dict), required=False) 

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'country_of_origin' })
    country_of_origin = forms.ChoiceField(label=_(u'Country of origin'), choices=choices.AFRICAN_COUNTRIES, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'country_of_residence' })
    country_of_residence = forms.ChoiceField(label=_(u'Country of residence'), choices=choices.AFRICAN_COUNTRIES, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'phone' })
    phone = forms.CharField(label=_(u'Phone no:'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({'class':'form-control required', 'placeholder':'Industry', 'name':'industry', 'type':'text', 'id':'id_industry', 'required':'true'})
    industry = forms.CharField(label=_(u'Industry'), max_length=30, widget=forms.TextInput(attrs=attrs_dict), required=True)

    attrs_dict = ({'class':'form-control required', 'placeholder':'Company', 'name':'company', 'type':'text', 'id':'id_company', 'required':'true'})
    company = forms.CharField(label=_(u'Company'), max_length=30, widget=forms.TextInput(attrs=attrs_dict), required=True)

    class Meta:
        model = get_profile_model()
        exclude = ['user', 'privacy', 'drive', 'skills']

    def __init__(self, *args, **kw):
        """
        Get the mugshot  and identification at the top of the form.
        """
        super(EditOfferrerProfileForm, self).__init__(*args, **kw)
        self.fields.insert(0,'mugshot', self.fields['mugshot'])
        self.fields.insert(1,'identification', self.fields['identification'])

    def save(self, force_insert=False, force = False, commit=True):
        profile = super(EditOfferrerProfileForm, self).save(commit=commit)
        profile.mugshot = self.cleaned_data['mugshot']
        profile.save()
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return profile


class EditFreelancerProfileForm(EditProfileForm):
    attrs_dict = {}

    mugshot = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'id_mugshot'}), required=False)

    identification = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'id_identification'}), required=False)

    attrs_dict = ({'class':'form-control required', 'placeholder':'First Name', 'name':'first_name', 'type':'text', 'id':'id_first_name', 'required':'true'})
    first_name = forms.CharField(label=_(u'First name'), max_length=30, widget=forms.TextInput(attrs=attrs_dict), required=True)

    attrs_dict = ({'class':'form-control required', 'placeholder':'Last Name', 'name':'last_name', 'type':'text', 'id':'id_last_name', 'required':'true'})
    last_name = forms.CharField(label=_(u'Last name'), max_length=30, widget=forms.TextInput(attrs=attrs_dict), required=True)
    
    attrs_dict = ({  'class': 'form-control required', 'name': 'gender' })
    gender = forms.ChoiceField(label=_(u'Gender'),choices=choices.GENDER_CHOICES, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'date', 'class': 'form-control', 'name': 'birth_date'})
    birth_date = forms.DateField(label=_(u'Birth Date'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({  'class': 'form-control required', 'name': 'profile_type' })
    profile_type = forms.ChoiceField(label=_(u'I am here as a'), choices=choices.PROFILE_TYPE, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'location' })
    location = forms.CharField(label=_(u'Location'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({'class': 'form-control', 'cols': '30', 'rows': '5', 'name': 'bio', 'style': 'resize: vertical', 'maxlength':'250'})
    bio = forms.CharField(label=_(u'Short awesome self-description (max. 250 words)'), max_length=250, widget=forms.Textarea(attrs=attrs_dict), required=False)   
    
    attrs_dict = ({'class': 'form-control', 'cols': '30', 'rows': '5', 'name': 'drive', 'style': 'resize: vertical', 'maxlength':'100'})
    drive = forms.CharField(label=_(u'What drives you as a freelancer?'), max_length=100, widget=forms.Textarea(attrs=attrs_dict), required=False)   

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'country_of_origin' })
    country_of_origin = forms.ChoiceField(label=_(u'Country of origin'), choices=choices.AFRICAN_COUNTRIES, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'country_of_residence' })
    country_of_residence = forms.ChoiceField(label=_(u'Country of residence'), choices=choices.AFRICAN_COUNTRIES, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'phone' })
    phone = forms.CharField(label=_(u'Phone no:'), widget=forms.TextInput(attrs=attrs_dict), required=False)
    
    class Meta:
        model = get_profile_model()
        exclude = ['user', 'privacy', 'industry', 'company', 'skills']

    def __init__(self, *args, **kw):
        """
        Get the mugshot  and identification at the top of the form.
        """
        super(EditFreelancerProfileForm, self).__init__(*args, **kw)
        self.fields.insert(0,'mugshot', self.fields['mugshot'])
        self.fields.insert(1,'identification', self.fields['identification'])

    def save(self, force_insert=False, force = False, commit=True):
        profile = super(EditFreelancerProfileForm, self).save(commit=commit)
        profile.mugshot = self.cleaned_data['mugshot']
        profile.save()
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return profile
