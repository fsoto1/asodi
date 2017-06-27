from django import forms
from sas.models import Socio
from functools import partial
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())

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