from django import forms
from main.models import Show, User, Episode

class ShowForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the show title.")
	# NOTE: as an alternative to specifying what fields to include with a forms call, you can do exclude = ('field_to_exclude', ) to exclude a specific one

	# An inline class to provide additional information on the form.
	class Meta:
		# provide an association between the ModelForm and a model
	 	model = Show
	 	fields = ('title',)



