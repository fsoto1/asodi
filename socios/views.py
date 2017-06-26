from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from sas.models import Socio
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import SocioForm
# Create your views here.



def buscar(request):
	if not request.user.is_authenticated:
		return redirect('sas:login')

	#return Socios.objects.all().filter(rut_socios='%2')
	#return Socios.objects.filter(rut_socios__contains='2')
	#return Socios.objects.filter(rut_socios__startswith='2')
	#Q(rut_socios__startswith='2') |
	#		Q(nom_socios__startswith='A')
	print("get")
	all_socios = Socio.objects.all()
	
	query = request.GET.get("q")
	if query:
		print("query")
		all_socios = all_socios.filter(
			Q(rut_socio__icontains=query) |
			Q(nom_socio__icontains=query) |
			Q(apel_pat_socio__icontains=query) |
			Q(apel_mat_socio__icontains=query)
			).distinct()
	
		
		#return render(request,'socios/buscar_socios.html', {'all_socios': all_socios} )
	return render(request,'socios/buscar_socios.html', {'all_socios': all_socios})

def socio(request):
	if not request.user.is_authenticated:
		return redirect('sas:login')		
	query = request.GET.get("id")
	if query:
		print("query")
		socio = Socio.objects.get(id_socio = query)
	return render(request, 'socios/socio.html', {'socio': socio})


def agregar_socio(request):
	form = SocioForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"form":form,
	}
	return render(request, "socios/agregar_socio.html", context)