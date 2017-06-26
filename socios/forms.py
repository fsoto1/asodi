from django import forms
from sas.models import Socio

class SocioForm(forms.ModelForm):
	rut_socio = forms.CharField(label='Rut')
	email_socio = forms.CharField(label='E-mail',widget=forms.EmailInput)
	fech_nac_socio = forms.CharField(label='Fecha Nacimiento',widget=forms.DateTimeInput)
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
			"fech_ing_socio",
			"id_estado",
			"id_est_civil",
			"id_salud",
			"id_ctro_salud",
			"id_prev",
			"id_patologia",
			#"id_apoderado",
			"id_tipo_paciente",
			"fech_defun",
		]
