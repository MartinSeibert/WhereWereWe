from django import forms
from django.contrib.auth.models import User
from main.models import Show, User, Episode, UserProfile
from django.template.defaultfilters import slugify

class ShowForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the show title.")
	# NOTE: as an alternative to specifying what fields to include with a forms call, you can do exclude = ('field_to_exclude', ) to exclude a specific one


	# This custom clean method checks whether or not the show already exists in the database, and if it does, then it raises an error on the title field
	def clean(self):		
		data = self.cleaned_data
		show = Show.objects.filter(slug = slugify(data['title'])).first()

		if show is not None:			
			self.add_error('title', 'That title has already been added!')

	# An inline class to provide additional information on the form.
	class Meta:
		# provide an association between the ModelForm and a model
	 	model = Show
	 	fields = ('title',)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)


