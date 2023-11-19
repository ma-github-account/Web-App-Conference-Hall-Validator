from django import forms
from .models import Conf_hall
from django.forms import ModelForm

#class NameForm(forms.Form):
#    
#	name = forms.CharField(label='Name', max_length=100)
#	second_name = forms.CharField(label='Second_name', max_length=100)


#class conf_hallForm(forms.ModelForm):
#
#	class Meta:
#
#		model = conf_hall
#		fields = ('name', 'second_name')

class conf_hallForm(ModelForm):

	class Meta:
		model = Conf_hall
		fields = '__all__'


















