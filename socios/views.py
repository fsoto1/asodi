from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Socios
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

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
	all_socios = Socios.objects.all()
	
	query = request.GET.get("q")
	if query:
		print("query")
		all_socios = all_socios.filter(
			Q(rut_socios__icontains=query) |
			Q(nom_socios__icontains=query) |
			Q(apel_pat_socios__icontains=query) |
			Q(apel_mat_socios__icontains=query)
			).distinct()
	
	paginator = Paginator(all_socios,10)
	page = request.GET.get("page")
	print("try")
	try:
		all_socios = paginator.page(page)
		print("queryset")
	except PageNotAnInteger:
		all_socios = paginator.page(1)
		print("PageNotAnInteger")
	except EmptyPage:
		all_socios = paginator.page(paginator.num_pages)
		print("EmptyPage")
	return render(request,'socios/buscar_socios.html', {'all_socios': all_socios} )

def socio(request):
	if not request.user.is_authenticated:
		return redirect('sas:login')		
	query = request.GET.get("id")
	if query:
		print("query")
		socio = Socios.objects.get(id_socios = query)
	return render(request, 'socios/socio.html', {'socio': socio})