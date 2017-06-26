from django.contrib import admin
from .models import Apoderado, Comuna, CtroSalud, Cuota, EstCivil, Estado, Pago, Patologia, Prevision, Provincia, Region, Salud, Socio, TipoPaciente

class ApoderadoAdmin(admin.ModelAdmin):
    list_display = ["nom_apoderado","apel_pat_apoderado","rut_apoderado", "id_socio"]
    list_filter = ["fech_ing_apod"]
    search_fields = ["nom_apoderado","apel_pat_apoderado","rut_apoderado"]
    raw_id_fields= ["id_socio", "comuna_numero"]
    class Meta:
    	Apoderado

admin.site.register(Apoderado, ApoderadoAdmin)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ["com_nom","provincia_prov_cod"]
    search_fields = ["com_nom"]
    class Meta:
    	Comuna

admin.site.register(Comuna, ComunaAdmin)

class CtroSaludAdmin(admin.ModelAdmin):
    list_display = ["nom_ctro_salud","telef_ctro_salud","med_ctro_salud","enf_ctro_salud", "comuna_numero"]
    search_fields = ["nom_ctro_salud"]
    class Meta:
    	CtroSalud

admin.site.register(CtroSalud, CtroSaludAdmin)

class CuotaAdmin(admin.ModelAdmin):
    list_display = ["id_cuota","fecha_emision"]
    list_filter = ["fecha_emision"]
    search_fields = ["id_cuota","fecha_emision"]
    class Meta:
    	Cuota

admin.site.register(Cuota, CuotaAdmin)

class EstCivilAdmin(admin.ModelAdmin):
    list_display = ["nom_est_civil"]
    search_fields = ["nom_est_civil"]

    class Meta:
    	EstCivil

admin.site.register(EstCivil, EstCivilAdmin)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ["nom_estado"]
    search_fields = ["nom_estado"]
    class Meta:
    	Estado

admin.site.register(Estado, EstadoAdmin)

class PagoAdmin(admin.ModelAdmin):
    list_display = ["id_pago","id_socio","id_cuota","monto","fecha_pago"]
    search_fields = ["id_pago","id_socio","id_cuota","fecha_pago"]
    list_filter = ["fecha_pago"]
    raw_id_fields= ["id_socio","id_cuota"]
    class Meta:
    	Pago

admin.site.register(Pago, PagoAdmin)

class PatologiaAdmin(admin.ModelAdmin):
    list_display = ["nom_patologia"]
    search_fields = ["nom_patologia"]
    class Meta:
    	Patologia

admin.site.register(Patologia, PatologiaAdmin)

class PrevisionAdmin(admin.ModelAdmin):
    list_display = ["nom_prevision"]
    search_fields = ["nom_prevision"]
    class Meta:
    	Prevision

admin.site.register(Prevision, PrevisionAdmin)

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ["prov_nombre","region_region_numero"]
    search_fields = ["prov_nombre"]
    class Meta:
    	Provincia

admin.site.register(Provincia, ProvinciaAdmin)

class RegionAdmin(admin.ModelAdmin):
    list_display = ["nombre_region"]
    search_fields = ["nombre_region"]
    class Meta:
    	Region

admin.site.register(Region, RegionAdmin)

class SaludAdmin(admin.ModelAdmin):
    list_display = ["nom_salud"]
    search_fields = ["nom_salud"]
    class Meta:
    	Salud

admin.site.register(Salud, SaludAdmin)

class SocioAdmin(admin.ModelAdmin):
    list_display = ["rut_socio","nom_socio","apel_pat_socio","apel_mat_socio","id_estado", "id_tipo_paciente"]
    list_filter = ["fech_nac_socio","fech_ing_socio","fech_defun"]
    search_fields = ["rut_socio","nom_socio","apel_pat_socio","apel_mat_socio"]
    raw_id_fields= ["id_ctro_salud","id_comuna","id_estado", "id_est_civil","id_salud","id_prev","id_patologia", "id_tipo_paciente"]
    class Meta:
    	Socio

admin.site.register(Socio, SocioAdmin)

class TipoPacienteAdmin(admin.ModelAdmin):
    list_display = ["nom_tipo_pacientes"]
    search_fields = ["nom_tipo_pacientes"]
    class Meta:
    	TipoPaciente

admin.site.register(TipoPaciente, TipoPacienteAdmin)