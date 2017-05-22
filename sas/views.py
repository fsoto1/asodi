from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.views.generic import View

from .forms import UserLoginForm


class LoginView(View):
	form_class = UserLoginForm
	template_name = 'sas/login.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		print('REQUEST') 
		print(request.POST) 
		form = self.form_class(request.POST or None)
		print('POST') 
		if form.is_valid():
			print('FORM') 
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				print('NOT NONE') 
				login(request,user)
				return redirect('sas:index')
			else:
				print('NONE')
				print(form.errors.as_data()) 
				print(username) 
		else:
				print('INVALID FORM') 
				print(form.errors.as_data()) 
		return render(request, self.template_name, {'form': form})

def logout_view(request):
	logout(request)
	return redirect('sas:login')

class IndexView(TemplateView):
	template_name = 'sas/home.html'

class IngresarSocioView(TemplateView):
	template_name = 'sas/ingresar-socio.html'
