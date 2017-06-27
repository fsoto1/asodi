from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from sas.models import Socio, Apoderado
from django.db.models import Q
from .forms import SocioForm, ApoderadoForm
# Create your views here.



def socio_list(request):
	if not request.user.is_authenticated:
		return redirect('login:login')

	all_socios = Socio.objects.all()
	
	query = request.GET.get("q")
	if query:
		all_socios = all_socios.filter(
			Q(rut_socio__icontains=query) |
			Q(nom_socio__icontains=query) |
			Q(apel_pat_socio__icontains=query) |
			Q(apel_mat_socio__icontains=query)
			).distinct()
	return render(request,'socios/buscar_socios.html', {'all_socios': all_socios})


def socio_detail(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	socio = get_object_or_404(Socio, id=id)	
	form = SocioForm(request.POST or None, instance=socio)
	context = {
		"socio": socio,
		"form": form,
	}
	return render(request, 'socios/detalle_socio.html', context)

def socio_add(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	form = SocioForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Socio agregado correctamente", extra_tags='list-group-item list-group-item-success')
		return redirect('socios:socio', id=(instance.id))
	context = {
		"form":form,
	}
	return render(request, "socios/form_socio.html", context)

def socio_edit(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Socio, id=id)		
	form = SocioForm(request.POST or None, instance= instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Modificado correctamente", extra_tags='list-group-item list-group-item-success')
		return redirect('socios:socio', id=(id))
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'socios/form_socio.html', context)

def socio_delete(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Socio, id=id)
	instance.delete()
	messages.success(request, "Eliminado correctamente", extra_tags='list-group-item list-group-item-success')
	return redirect("socios:buscar-socios")


def apoderado_list(request):
	if not request.user.is_authenticated:
		return redirect('login:login')

	all_apoderados = Apoderado.objects.all()
	
	query = request.GET.get("q")
	if query:
		all_apoderados = all_apoderados.filter(
			Q(rut_apoderado__icontains=query) |
			Q(nom_apoderado__icontains=query) |
			Q(apel_pat_apoderado__icontains=query) |
			Q(apel_mat_apoderado__icontains=query)
			).distinct()
	return render(request,'socios/buscar_apoderado.html', {'all_apoderados': all_apoderados})


def apoderado_detail(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	apoderado = get_object_or_404(Apoderado, id=id)	
	form = ApoderadoForm(request.POST or None, instance=apoderado)
	context = {
		"apoderado": apoderado,
		"form": form,
	}
	return render(request, 'socios/detalle_apoderado.html', context)

def apoderado_add(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	form = ApoderadoForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Apoderado agregado correctamente", extra_tags='list-group-item list-group-item-success')
		return redirect('socios:apoderado', id=(instance.id))
	context = {
		"form":form,
	}
	return render(request, "socios/form_apoderado.html", context)

def apoderado_edit(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Apoderado, id=id)		
	form = ApoderadoForm(request.POST or None, instance= instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Modificado correctamente", extra_tags='list-group-item list-group-item-success')
		return redirect('socios:apoderado', id=(id))
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'socios/form_apoderado.html', context)

def apoderado_delete(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Apoderado, id=id)
	instance.delete()
	messages.success(request, "Eliminado correctamente", extra_tags='list-group-item list-group-item-success')
	return redirect("socios:buscar-apoderado")