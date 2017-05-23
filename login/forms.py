from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms


class UserLoginForm(forms.Form):
	username = forms.CharField(label='Usuario')
	password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = ['username', 'password']

	def clean(self):
         cleaned_data = super(UserLoginForm, self).clean()
         username = cleaned_data.get("username")
         password = cleaned_data.get("password")
         user = authenticate(username=username, password=password)
         if not user or not user.is_active:
            raise forms.ValidationError("Usuario o Contraseña incorrectas")