# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Apoderado(models.Model):
    rut_apoderado = models.CharField(max_length=10, blank=True, null=True)
    nom_apoderado = models.CharField(max_length=45, blank=True, null=True)
    apel_pat_apoderado = models.CharField(max_length=45, blank=True, null=True)
    apel_mat_apoderado = models.CharField(max_length=45, blank=True, null=True)
    email_apoderado = models.CharField(max_length=45, blank=True, null=True)
    telef_apoderado = models.CharField(max_length=45, blank=True, null=True)
    fech_nac_apoderado = models.DateField(blank=True, null=True)
    comuna_numero = models.ForeignKey('Comuna',  on_delete=models.CASCADE)
    dir_apoderado = models.CharField(max_length=45, blank=True, null=True)
    fech_ing_apod = models.DateField(auto_now_add=True, blank=True, null=True)
    id_socio = models.ForeignKey('Socio',  on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rut_apoderado

    


class Comuna(models.Model):
    com_nom = models.CharField(max_length=45)
    provincia_prov_cod = models.ForeignKey('Provincia',  on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.com_nom

    class Meta:
        ordering = ["com_nom"]


class CtroSalud(models.Model):
    nom_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    dir_ctro_salud = models.CharField(max_length=60, blank=True, null=True)
    rut_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    comuna_numero = models.ForeignKey(Comuna,  on_delete=models.CASCADE)
    telef_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    email_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    med_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    enf_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_ctro_salud

    class Meta:
        verbose_name_plural = "Centros de Salud"


class Cuota(models.Model):
    fecha_emision = models.DateField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.fecha_emision)




class EstCivil(models.Model):
    nom_est_civil = models.CharField(max_length=45, blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nom_est_civil

    class Meta:
        ordering = ["nom_est_civil"]
        verbose_name_plural = "Estados Civiles"


class Estado(models.Model):
    nom_estado = models.CharField(max_length=45)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nom_estado

    class Meta:
        ordering = ["nom_estado"]

class Pago(models.Model):
    id_socio = models.ForeignKey('Socio',  on_delete=models.CASCADE)
    id_cuota = models.ForeignKey(Cuota,  on_delete=models.CASCADE)
    monto = models.IntegerField()
    fecha_pago = models.DateField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.id)



class Patologia(models.Model):
    nom_patologia = models.CharField(max_length=45)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nom_patologia




class Prevision(models.Model):
    nom_prevision = models.CharField(max_length=45, blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nom_prevision

    class Meta:

        verbose_name_plural = "Previsiones"


class Provincia(models.Model):
    prov_nombre = models.CharField(max_length=45)
    region_region_numero = models.ForeignKey('Region',  on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.prov_nombre



class Region(models.Model):
    nombre_region = models.CharField(max_length=45)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nombre_region

    class Meta:
        verbose_name_plural = "Regiones"


class Salud(models.Model):
    nom_salud = models.CharField(max_length=45, blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nom_salud

    class Meta:
        verbose_name_plural = "Salud"

class Socio(models.Model):
    rut_socio = models.CharField(max_length=10, blank=True, null=True)
    sexo_socio = models.CharField(max_length=1, blank=True, null=True)
    nom_socio = models.CharField(max_length=45, blank=True, null=True)
    apel_pat_socio = models.CharField(max_length=45, blank=True, null=True)
    apel_mat_socio = models.CharField(max_length=45, blank=True, null=True)
    dir_socio = models.CharField(max_length=45, blank=True, null=True)
    email_socio = models.CharField(max_length=45, blank=True, null=True)
    telef_socio = models.CharField(max_length=45, blank=True, null=True)
    cel_socio = models.CharField(max_length=45, blank=True, null=True)
    fech_nac_socio = models.DateField(blank=True, null=True)
    foto_socio = models.CharField(max_length=45, blank=True, null=True)
    id_comuna = models.ForeignKey(Comuna,  on_delete=models.CASCADE)
    fech_ing_socio = models.DateField(auto_now_add=True, blank=True, null=True)
    id_estado = models.ForeignKey(Estado,  on_delete=models.CASCADE)
    id_est_civil = models.ForeignKey(EstCivil,  on_delete=models.CASCADE, blank=True, null=True)
    id_salud = models.ForeignKey(Salud,  on_delete=models.CASCADE, blank=True, null=True)
    id_ctro_salud = models.ForeignKey(CtroSalud,  on_delete=models.CASCADE)
    id_prev = models.ForeignKey(Prevision,  on_delete=models.CASCADE)
    id_patologia = models.ForeignKey(Patologia,  on_delete=models.CASCADE)
    id_tipo_paciente = models.ForeignKey('TipoPaciente',  on_delete=models.CASCADE)
    fech_defun = models.DateField(blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.rut_socio



class TipoPaciente(models.Model):
    nom_tipo_pacientes = models.CharField(max_length=45, blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nom_tipo_pacientes

    class Meta:
        verbose_name_plural = "Tipos de Pacientes"
