from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def index(request):
	if not request.user.is_authenticated:
		return redirect('login:login')	
	return render(request, 'sas/home.html')


