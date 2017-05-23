from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.

def buscar_socios(request):
	if not request.user.is_authenticated:
		return redirect('sas:login')
	else:	
		return render(request, 'socios/buscar_socios.html')