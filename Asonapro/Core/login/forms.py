from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .views import*
from Core.User.models import Sembradores


class ResetPassWordForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Ingrese un usuario',
				'class': 'form-control',
				'autocomplete': 'off'
		}))

	def clean(self):
		cleaned = super().clean()

		if not Sembradores.objects.filter(username=cleaned['username']).exists():
			self._errors['error'] = self._errors.get('error', self.error_class())
			self._errors['error'].append('El usuario no exixte')
			#raise forms.ValidationError('El usuario no existe')
		
		return cleaned		


	def get_user(self):
		username = self.cleaned_data.get('username')
		return Sembradores.objects.get(username=username)




class ChangedPassWordForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Ingrese una contraseña',
		'class': 'form-control',
		'autocomplete': 'off'
		}))

	confirmarPassword = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'repita la contraseña',
		'class': 'form-control',
		'autocomplete': 'off'
		}))

	def clean(self):
		cleaned = super().clean()
		password = cleaned['password']
		confirmarPassword = cleaned['confirmarPassword']

		if password != confirmarPassword:
			self._errors['error'] = self._errors.get('error', self.error_class())
			self._errors['error'].append('Las contraseñas deben ser iguales')

			#raise forms.ValidationError('las contraseñas deben ser iguales')
	
		return cleaned