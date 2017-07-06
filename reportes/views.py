from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from sas.models import Comuna, Apoderado, Socio
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
import xlwt

def reportes(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	if not request.user.is_staff or not request.user.is_superuser:
		return render(request, 'sas/sin_permisos.html')

	return render(request,'reportes/reportes.html')

def comunas(request):
	if not request.user.is_authenticated:
		return redirect('login:login')
	if not request.user.is_staff or not request.user.is_superuser:
		return render(request, 'sas/sin_permisos.html')


	obj = Socio.objects.all()


	#obj = obj.filter(
	#	id_socio=6
	#	).distinct() 
	#Book.objects.select_related('author__hometown').get(id=4)
	obj = obj.values('id_comuna').annotate(total=Count('id_socio')).order_by('id_comuna')


	for o in obj:
		print (o)

 
	#.values('actor').annotate(total=Count('actor')).order_by('total')
	paginator = Paginator(obj,25)
	page = request.GET.get("page")
	try:
		obj = paginator.page(page)
	except PageNotAnInteger:
		obj = paginator.page(1)
	except EmptyPage:
		obj = paginator.page(paginator.num_pages)
	return render(request,'reportes/comunas.html', {'obj': obj})

def export_socios(request):
	if not request.user.is_authenticated:
		return redirect('login:login')

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="comuna.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Comunas')

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
