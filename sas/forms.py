
from django.contrib.auth.models import User
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
         print(self.cleaned_data)
         if username and password:
            # Only do something if both fields are valid so far.
             if "a" not in password:
             	   raise forms.ValidationError("NOOOO")
                   
