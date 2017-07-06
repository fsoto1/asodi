from django import forms
from sas.models import Socio, Apoderado, Comuna, Estado, CtroSalud, EstCivil, Patologia,Prevision, TipoPaciente, Salud
from functools import partial



DateInput = partial(forms.DateInput, {'class': 'datepicker'})


Sexo = (
	('M', "Masculino"),
	('F', "Femenino"),
	)
    

class SocioForm(forms.ModelForm):
	rut_socio = forms.CharField(label='Rut')
	email_socio = forms.CharField(label='E-mail',widget=forms.EmailInput)
	fech_nac_socio = forms.DateField(label='Fecha de Nacimiento', widget=DateInput())
	sexo_socio = forms.ChoiceField(choices=Sexo, label='Sexo')
	nom_socio = forms.CharField(label='Nombre')
	apel_pat_socio = forms.CharField(label='Apellido Paterno')
	apel_mat_socio = forms.CharField(label='Apellido Materno', required=False)
	dir_socio = forms.CharField(label='Dirección')
	telef_socio = forms.CharField(label='Teléfono', required=False)
	cel_socio = forms.CharField(label='Celular', required=False)
	id_comuna = forms.ModelChoiceField(label='Comuna', queryset=Comuna.objects.all())
	id_estado = forms.ModelChoiceField(label='Estado Socio', queryset=Estado.objects.all())
	id_est_civil = forms.ModelChoiceField(label='Estado Civil', queryset=EstCivil.objects.all())
	id_salud = forms.ModelChoiceField(label='Sistema de Salud', queryset=Salud.objects.all())
	id_ctro_salud = forms.ModelChoiceField(label='Centro de Salud', queryset=CtroSalud.objects.all())
	id_prev = forms.ModelChoiceField(label='Previsión', queryset=Prevision.objects.all())
	id_patologia = forms.ModelChoiceField(label='Patología', queryset=Patologia.objects.all())
	id_tipo_paciente = forms.ModelChoiceField(label='Tipo de Paciente', queryset=TipoPaciente.objects.all())
    

	class Meta:
		model = Socio
		fields=[
			"rut_socio",
			"sexo_socio",
			"nom_socio",
			"apel_pat_socio",
			"apel_mat_socio",
			"dir_socio",
			"email_socio",
			"telef_socio",
			"cel_socio",
			"fech_nac_socio",
			"id_comuna",
			"id_estado",
			"id_est_civil",
			"id_salud",
			"id_ctro_salud",
			"id_prev",
			"id_patologia",
			"id_tipo_paciente",
		]


class ApoderadoForm(forms.ModelForm):
	rut_apoderado = forms.CharField(label='Rut')
	email_apoderado = forms.CharField(label='E-mail',widget=forms.EmailInput, required=False)
	fech_nac_apoderado = forms.DateField(label='Fecha de Nacimiento',widget=DateInput())
	fech_ing_apod = forms.DateField(label='Fecha de Ingreso',widget=DateInput())
	id_socio = forms.ModelChoiceField(label='Socio', queryset=Socio.objects.all())
	nom_apoderado = forms.CharField(label='Nombre')
	apel_pat_apoderado = forms.CharField(label='Apellido Paterno')
	apel_mat_apoderado = forms.CharField(label='Apellido Materno', required=False)
	telef_apoderado = forms.CharField(label='Teléfono', required=False)
	comuna_numero = forms.ModelChoiceField(label='Comuna', queryset=Comuna.objects.all())
	dir_apoderado = forms.CharField(label='Dirección')



	class Meta:
		model = Apoderado
		fields=[
			"rut_apoderado",
			"nom_apoderado",
			"apel_pat_apoderado",
			"apel_mat_apoderado",
			"email_apoderado",
			"telef_apoderado",
			"fech_nac_apoderado",
			"comuna_numero",
			"dir_apoderado",
			"fech_ing_apod",
			"id_socio",
		]

