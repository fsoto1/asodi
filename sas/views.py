from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def index(request):
	if not request.user.is_authenticated:
		return redirect('sas:login')	
	if not request.user.is_staff or not request.user.is_superuser:
		return render(request, 'sas/sin_permisos.html')
	return render(request, 'sas/home.html')


