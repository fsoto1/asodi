from django import forms
from sas.models import Socio, Apoderado
from functools import partial
from itertools import cycle


DateInput = partial(forms.DateInput, {'class': 'datepicker'})


Sexo = (
	('M', "Masculino"),
	('F', "Femenino"),
	)
    

class SocioForm(forms.ModelForm):
	rut_socio = forms.CharField(label='Rut')
	email_socio = forms.CharField(label='E-mail',widget=forms.EmailInput)
	fech_nac_socio = forms.DateField(widget=DateInput())
	sexo_socio = forms.ChoiceField(choices=Sexo, label='Sexo')

    

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
			"foto_socio",
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
	email_apoderado = forms.CharField(label='E-mail',widget=forms.EmailInput)
	fech_nac_apoderado = forms.DateField(widget=DateInput())

    

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
			"id_socio",
		]

		