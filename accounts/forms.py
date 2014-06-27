from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from userena.forms import SignupFormTos, AuthenticationForm, ChangeEmailForm, EditProfileForm
from userena.utils import get_profile_model
USERNAME_RE = r'^[\.\w]+$'


class SignupFormExtra(SignupFormTos):
    """
    Adding extra first and last name fields to the signup form.

    """
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required', 
        'placeholder':'First Name',
        'name':'first_name',
        'type':'text',
        'id':'id_first_name',
        'required':'true'})
    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 widget=forms.TextInput(attrs=attrs_dict),
                                 required=False)    

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Last Name',
        'name':'last_name',
        'type':'text',
        'id':'id_last_name',
        'required':'true'})
    last_name = forms.CharField(label=_(u'Last name'),
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                required=False)

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Username',
        'name':'username',
        'type':'text',
        'required':'true',
        'id':'id_username'  })
    username = forms.RegexField(regex=USERNAME_RE,
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={'invalid': _('Username must contain only letters, numbers, dots and underscores.')})

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Email',
        'name':'email',
        'type':'email', 
        'required':'true', 
        'id':'id_email'})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("Email"))

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Password',
        'name':'password1',
        'type':'password',
        'id':'id_password1'})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Create password"))

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Confirm password',
        'name':'password2',
        'type':'password',
        'id':'id_password2'})
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Repeat password"))



    def __init__(self, *args, **kw):
        """
        Get the first name and last name at the top of the
        form instead of being at the end.
        """
        super(SignupFormExtra, self).__init__(*args, **kw)
        # Put the first and last name at the top
        new_order = self.fields.keyOrder[:-2]
        new_order.insert(0, 'first_name')
        new_order.insert(1, 'last_name')
        self.fields.keyOrder = new_order

    def save(self):
        """
        Overriding the save method to save the first and last name to the user
        field.
        """
        # First save the parent form and get the user.
        new_user = super(SignupFormExtra, self).save()

        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.save()
        # Userena expects to get the new user from this form, so return the new
        # user.
        return new_user


class AuthenticationFormExtra(AuthenticationForm):
    """
    Styling AuthenticationForm with bootstrap.
    """
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required', 
        'placeholder':'Email or username',
        'name':'identification',
        'type':'text',
        'id':'id_identification',
        'required':'true'})
    identification = forms.CharField(label=_(u'Email or username'),
                                 max_length=50,
                                 widget=forms.TextInput(attrs=attrs_dict),
                                 required=True)    

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Password',
        'name':'password',
        'type':'password',
        'id':'id_password'})
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Password"))   

class ChangeEmailFormExtra(ChangeEmailForm):
    """
    Styling ChangeEmailForm with bootstrap.
    """
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Email',
        'name':'email',
        'type':'email', 
        'required':'true', 
        'id':'id_email'})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("New Email")) 

class EditProfileFormExtra(EditProfileForm):
    
    attrs_dict = {}

    LEVEL = (
        (1, _('Registered')),
        (2, _('Open')),
        (3, _('Closed')),
    )

    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
        (3, _('None'))
    )

    mugshot = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'id_mugshot'}), required=False)

    attrs_dict = ({'class':'form-control required', 
        'placeholder':'First Name',
        'name':'first_name',
        'type':'text',
        'id':'id_first_name',
        'required':'true'})
    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 widget=forms.TextInput(attrs=attrs_dict),
                                 required=True)

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Last Name',
        'name':'last_name',
        'type':'text',
        'id':'id_last_name',
        'required':'true'})
    last_name = forms.CharField(label=_(u'Last name'),
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                required=True)
    
    attrs_dict = ({  'class': 'form-control required', 'name': 'gender' })
    gender = forms.ChoiceField(label=_(u'Gender'),choices=GENDER_CHOICES, widget=forms.Select(attrs=attrs_dict))

    attrs_dict = ({  
                    'type': 'date',
                    'class': 'form-control',
                    'name': 'birth_date'
                 })
    birth_date = forms.DateField(label=_(u'Birth Date'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'country_of_origin' })
    country_of_origin = forms.CharField(label=_(u'Country of origin'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'country_of_residence' })
    country_of_residence = forms.CharField(label=_(u'Country of residence'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'location' })
    location = forms.CharField(label=_(u'Location'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    attrs_dict = ({  
                    'class': 'form-control',
                    'cols': '30', 'rows': '5',
                    'name': 'bio' 
                 })
    bio = forms.CharField(label=_(u'Short bio about yourself'), widget=forms.Textarea(attrs=attrs_dict), required=False)   


    attrs_dict = ({'type': 'text', 'class': 'form-control', 'name': 'phone' })
    phone = forms.CharField(label=_(u'Phone no.'), widget=forms.TextInput(attrs=attrs_dict), required=False)

    class Meta:
        model = get_profile_model()
        exclude = ['user', 'privacy', 'profile_type']
        field = ['mugshot', 'first_name', 'last_name', 'gender', 'birth_date', 'country_of_origin', 'country_of_residence', 'location', 'bio', 'phone']

    def save(self, force_insert=False, force = False, commit=True):
        profile = super(EditProfileFormExtra, self).save(commit=commit)
        profile.mugshot = self.cleaned_data['mugshot']
        profile.save()
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return profile

class PasswordChangeFormExtra(PasswordChangeForm):

    error_messages = dict(PasswordChangeForm.error_messages)
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Old Password',
        'name':'old_password',
        'type':'password',
        'id':'old_password'})
    old_password = forms.CharField(label=_(u'Old Password'), widget=forms.PasswordInput(attrs=attrs_dict))
    
    attrs_dict = ({'class':'form-control required',
        'placeholder':'New Password',
        'name':'new_password1',
        'type':'password',
        'id':'id_new_password1'})
    new_password1 = forms.CharField(label=_(u'New Password'), widget=forms.PasswordInput(attrs=attrs_dict))
    

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Confirm New password',
        'name':'new_password2',
        'type':'password',
        'id':'id_new_password2'})
    new_password2 = forms.CharField(label=_(u'Confirm New Password'), widget=forms.PasswordInput(attrs=attrs_dict))

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user

class PasswordResetFormExtra(PasswordResetForm):
    attrs_dict = {}

    attrs_dict = ({'class':'form-control required',
        'placeholder':'Email',
        'name':'email',
        'type':'email', 
        'required':'true', 
        'id':'id_email'})
    email = forms.EmailField(label=_(u'Email'), widget=forms.TextInput(attrs=attrs_dict))