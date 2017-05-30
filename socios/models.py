from django.db import models
#from django.urls import reverse
#from django.forms import ModelForm
# Create your models here.


class Socios(models.Model):
    id_socios = models.AutoField(primary_key=True)
    cod_socios = models.CharField(max_length=15, blank=True, null=True)
    rut_socios = models.CharField(max_length=10, blank=True, null=True)
    sexo_socios = models.CharField(max_length=1, blank=True, null=True)
    nom_socios = models.CharField(max_length=45, blank=True, null=True)
    apel_pat_socios = models.CharField(max_length=45, blank=True, null=True)
    apel_mat_socios = models.CharField(max_length=45, blank=True, null=True)
    dir_socios = models.CharField(max_length=45, blank=True, null=True)
    email_socios = models.CharField(max_length=45, blank=True, null=True)
    telef_socios = models.CharField(max_length=45, blank=True, null=True)
    cel_socios = models.CharField(max_length=45, blank=True, null=True)
    fech_nac_socios = models.DateField(blank=True, null=True)
    foto_socios = models.CharField(max_length=45, blank=True, null=True)
    region_numero = models.IntegerField(blank=True, null=True)
    comuna_numero = models.IntegerField(blank=True, null=True)
    fech_ing_socios = models.DateField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_est_civil = models.IntegerField(blank=True, null=True)
    id_profesion = models.IntegerField(blank=True, null=True)
    id_salud = models.IntegerField(blank=True, null=True)
    id_ctro_salud = models.IntegerField(blank=True, null=True)
    id_prev = models.IntegerField(blank=True, null=True)
    id_perf = models.IntegerField(blank=True, null=True)
    id_patologia = models.IntegerField(blank=True, null=True)
    id_apoderado = models.IntegerField(blank=True, null=True)
    id_tipo_paciente = models.IntegerField(blank=True, null=True)
    fech_actu = models.DateTimeField(blank=True, null=True)
    log_usuario = models.IntegerField(blank=True, null=True)
    ciudad_numero = models.IntegerField(blank=True, null=True)
    fech_defun = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home:socios-add' )

    def __str__(self):
        return self.rut_socios
        
    class Meta:
        managed = False
        db_table = 'socios'