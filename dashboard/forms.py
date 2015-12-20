from django import forms
import autocomplete_light
autocomplete_light.autodiscover()
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from models import Nugget, Clustr


class SignupForm(RegistrationForm):
	email = forms.EmailField(label=("e-mail address"))
	username = forms.TextInput(attrs={'placeholder':'your email address'})
	class Meta:
		username = forms.TextInput(attrs={'placeholder':'your email address'})
		email = forms.EmailField(label=("e-mail address"))
	def __init__(self, *args, **kwargs):
		super(SignupForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

class ContributeForm(forms.Form):

	def __init__(self, *args, **kwargs):
		my_clustrs = kwargs.pop('my_clustrs')
		super(ContributeForm, self).__init__(*args, **kwargs)
		self.fields['clustr_box'].queryset=my_clustrs

	clustr_box = forms.ModelChoiceField(queryset='', label="which clustr would you like to contribute to?")
	text_or_nah = forms.ChoiceField(choices=(
		(True, 'textual'),
		(False, 'visual'),
		),
		label='is your nugget more text-based or more visual?')
	title = forms.CharField(max_length=100, label="what's the title of the article/video/song?")
	author = forms.CharField(max_length=100, label="who's the author/artist/creator?")
	source = forms.CharField(max_length=100, label="who published/produced it?")
	date = forms.CharField(max_length=100, label="when did it appear?")

class ClustrsSearchForm(forms.Form):
	clustr_input = autocomplete_light.ChoiceField('ClustrsSearchAutocomplete', label='')