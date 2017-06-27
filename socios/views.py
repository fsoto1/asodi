from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from sas.models import Socio
from django.db.models import Q
from .forms import SocioForm
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
	else:
		messages.error(request, "No se pudo agregar el socio", extra_tags='list-group-item list-group-item-danger')
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
	instance = get_object_or_404(Socio, id=id)
	instance.delete()
	messages.success(request, "Eliminado correctamente", extra_tags='list-group-item list-group-item-success')
	return redirect("socios:buscar-socios")