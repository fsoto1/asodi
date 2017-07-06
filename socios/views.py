from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from sas.models import Socio, Apoderado
from django.db.models import Q
from .forms import SocioForm, ApoderadoForm
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

def export_socios(request):
	if not request.user.is_authenticated:
		return redirect('login:login')

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="socios.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Socios')

	# Sheet header, first row
	row_num = 0

	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['ID', 'Rut', 'Sexo', 'Nombre', 'Apellido Paterno', 'Apellido Materno',
				 'Dirección', 'Email', 'Telefono', 'Celular', 'Fecha de Nacimiento', 'Comuna', 'Fecha ingreso',
				'Estado', 'Estado Civil', 'Sistema de Salud', 'Centro de Salud', 'Prevision','Patología', 'Tipo de paciente', 'Fecha de defunción' ]

	for col_num in range(len(columns)):
	    ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
	query = request.GET.get("q")
	rows = Socio.objects.all().values_list('id_socio', 
											'rut_socio',
											'sexo_socio',
											'nom_socio',
											'apel_pat_socio', 
											'apel_mat_socio',
											'dir_socio',
											'email_socio',
											'telef_socio',
											'cel_socio' ,
											'fech_nac_socio',
											'id_comuna' ,
											'fech_ing_socio',
											'id_estado' ,
											'id_est_civil',
											'id_salud' ,
											'id_ctro_salud',
											'id_prev' ,
											'id_patologia' ,
											'id_tipo_paciente',
											'fech_defun' 
		).filter(
			Q(rut_socio__icontains=query) |
			Q(nom_socio__icontains=query) |
			Q(apel_pat_socio__icontains=query) |
			Q(apel_mat_socio__icontains=query)
			).distinct()
	query = request.GET.get("q")

	for row in rows:
	    row_num += 1
	    for col_num in range(len(row)):
	    	if col_num == 10 or col_num == 12 or col_num == 20:
	    		ws.write(row_num, col_num, row[col_num], date_format)
	    	else:
	        	ws.write(row_num, col_num, row[col_num], font_style)


	wb.save(response)
	return response


def export_apoderados(request):
	if not request.user.is_authenticated:
		return redirect('login:login')

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="apoderados.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Apoderados')
	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'
	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['ID', 'Rut', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Email', 'Telefono', 'Fecha de Nacimiento', 
				 'Comuna',   'Dirección', 'Fecha ingreso', 'Socio',]

	for col_num in range(len(columns)):
	    ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
	query = request.GET.get("q")
	rows = Apoderado.objects.all().values_list( 'id_apoderado',
												'rut_apoderado',
												'nom_apoderado',
												'apel_pat_apoderado',
												'apel_mat_apoderado',
												'email_apoderado',
												'telef_apoderado',
												'fech_nac_apoderado',
												'comuna_numero',
												'dir_apoderado',
												'fech_ing_apod',
												'id_socio',
		).filter(
			Q(rut_apoderado__icontains=query) |
			Q(nom_apoderado__icontains=query) |
			Q(apel_pat_apoderado__icontains=query) |
			Q(apel_mat_apoderado__icontains=query)
			).distinct()
	query = request.GET.get("q")

	for row in rows:
	    row_num += 1
	    for col_num in range(len(row)):
	    	if col_num == 7 or col_num == 10:
	    		ws.write(row_num, col_num, row[col_num], date_format)
	    	else:
	        	ws.write(row_num, col_num, row[col_num], font_style)

	wb.save(response)
	return response

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
		paginator = Paginator(all_socios,25)
		page = request.GET.get("page")
		try:
			all_socios = paginator.page(page)
		except PageNotAnInteger:
			all_socios = paginator.page(1)
		except EmptyPage:
			all_socios = paginator.page(paginator.num_pages)
	return render(request,'socios/buscar_socios.html', {'all_socios': all_socios})


def socio_detail(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	socio = get_object_or_404(Socio, id_socio=id)	
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
		return redirect('socios:socio', id_socio=(instance.id))
	context = {
		"form":form,
	}
	return render(request, "socios/form_socio.html", context)

def socio_edit(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Socio, id_socio=id)		
	form = SocioForm(request.POST or None, instance= instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Modificado correctamente", extra_tags='list-group-item list-group-item-success')
		return redirect('socios:socio', id_socio=(id))
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'socios/form_socio.html', context)

def socio_delete(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Socio, id_socio=id)
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
		paginator = Paginator(all_apoderados,25)
		page = request.GET.get("page")
		print("try")
		try:
			all_apoderados = paginator.page(page)
			print("queryset")
		except PageNotAnInteger:
			all_apoderados = paginator.page(1)
			print("PageNotAnInteger")
		except EmptyPage:
			all_apoderados = paginator.page(paginator.num_pages)
			print("EmptyPage")
	return render(request,'socios/buscar_apoderado.html', {'all_apoderados': all_apoderados})


def apoderado_detail(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	apoderado = get_object_or_404(Apoderado, id_apoderado=id)	
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
		return redirect('socios:apoderado', id_apoderado=(instance.id))
	context = {
		"form":form,
	}
	return render(request, "socios/form_apoderado.html", context)

def apoderado_edit(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Apoderado, id_apoderado=id)		
	form = ApoderadoForm(request.POST or None, instance= instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Modificado correctamente", extra_tags='list-group-item list-group-item-success')
		return redirect('socios:apoderado', id_apoderado=(id))
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'socios/form_apoderado.html', context)

def apoderado_delete(request, id=None):
	if not request.user.is_authenticated:
		return redirect('login:login')
	instance = get_object_or_404(Apoderado, id_apoderado=id)
	instance.delete()
	messages.success(request, "Eliminado correctamente", extra_tags='list-group-item list-group-item-success')
	return redirect("socios:buscar-apoderado")