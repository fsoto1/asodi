from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserLoginForm

class LoginView(View):
	form_class = UserLoginForm
	template_name = 'login/login.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST or None)
		if form.is_valid():
			print('FORM') 
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None: 
				login(request,user)
				return redirect('sas:index')
		return render(request, self.template_name, {'form': form})

def logout_view(request):
	logout(request)
	return redirect('sas:login')