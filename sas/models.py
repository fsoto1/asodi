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
    id_apoderado = models.AutoField(primary_key=True)
    rut_apoderado = models.CharField(max_length=10, blank=True, null=True)
    nom_apoderado = models.CharField(max_length=45, blank=True, null=True)
    apel_pat_apoderado = models.CharField(max_length=45, blank=True, null=True)
    apel_mat_apoderado = models.CharField(max_length=45, blank=True, null=True)
    email_apoderado = models.CharField(max_length=45, blank=True, null=True)
    telef_apoderado = models.CharField(max_length=45, blank=True, null=True)
    fech_nac_apoderado = models.DateField(blank=True, null=True)
    comuna_numero = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna_numero', blank=True, null=True)
    dir_apoderado = models.CharField(max_length=45, blank=True, null=True)
    fech_ing_apod = models.DateField(blank=True, null=True)
    id_socio = models.ForeignKey('Socio', models.DO_NOTHING, db_column='id_socio', blank=True, null=True)

    def __str__(self):
        return self.rut_apoderado

    class Meta:
        managed = False
        db_table = 'apoderado'


class Comuna(models.Model):
    com_cod = models.AutoField(primary_key=True)
    com_nom = models.CharField(max_length=45)
    provincia_prov_cod = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='provincia_prov_cod')


    def __str__(self):
        return self.com_nom

    class Meta:
        managed = False
        db_table = 'comuna'
        ordering = ["com_nom"]


class CtroSalud(models.Model):
    id_ctro_salud = models.AutoField(primary_key=True)
    nom_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    dir_ctro_salud = models.CharField(max_length=60, blank=True, null=True)
    rut_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    comuna_numero = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_numero', blank=True, null=True)
    telef_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    email_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    med_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    enf_ctro_salud = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.nom_ctro_salud

    class Meta:
        managed = False
        db_table = 'ctro_salud'
        verbose_name_plural = "Centros de Salud"


class Cuota(models.Model):
    id_cuota = models.AutoField(primary_key=True)
    fecha_emision = models.DateField()

    def __str__(self):
            return str(self.id_cuota)

    class Meta:
        managed = False
        db_table = 'cuota'


class EstCivil(models.Model):
    id_est_civil = models.AutoField(primary_key=True)
    nom_est_civil = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
            return self.nom_est_civil

    class Meta:
        managed = False
        db_table = 'est_civil'
        ordering = ["nom_est_civil"]
        verbose_name_plural = "Estados Civiles"


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nom_estado = models.CharField(max_length=45)

    def __str__(self):
            return self.nom_estado

    class Meta:
        managed = False
        db_table = 'estado'
        ordering = ["nom_estado"]

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_socio = models.ForeignKey('Socio', models.DO_NOTHING, db_column='id_socio')
    id_cuota = models.ForeignKey(Cuota, models.DO_NOTHING, db_column='id_cuota')
    monto = models.IntegerField()
    fecha_pago = models.DateField()

    def __str__(self):
            return str(self.id_pago)

    class Meta:
        managed = False
        db_table = 'pago'

class Patologia(models.Model):
    id_patologia = models.AutoField(primary_key=True)
    nom_patologia = models.CharField(max_length=45)

    def __str__(self):
            return self.nom_patologia

    class Meta:
        managed = False
        db_table = 'patologia'


class Prevision(models.Model):
    id_prevision = models.AutoField(primary_key=True)
    nom_prevision = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
            return self.nom_prevision

    class Meta:
        managed = False
        db_table = 'prevision'
        verbose_name_plural = "Previsiones"


class Provincia(models.Model):
    prov_cod = models.AutoField(primary_key=True)
    prov_nombre = models.CharField(max_length=45)
    region_region_numero = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_region_numero')

    def __str__(self):
            return self.prov_nombre

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    region_numero = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=45)

    def __str__(self):
            return self.nombre_region

    class Meta:
        managed = False
        db_table = 'region'
        verbose_name_plural = "Regiones"


class Salud(models.Model):
    id_salud = models.AutoField(primary_key=True)
    nom_salud = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
            return self.nom_salud

    class Meta:
        managed = False
        db_table = 'salud'
        verbose_name_plural = "Salud"

class Socio(models.Model):
    id_socio = models.AutoField(primary_key=True)
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
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)
    fech_ing_socio = models.DateField(blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    id_est_civil = models.ForeignKey(EstCivil, models.DO_NOTHING, db_column='id_est_civil', blank=True, null=True)
    id_salud = models.ForeignKey(Salud, models.DO_NOTHING, db_column='id_salud', blank=True, null=True)
    id_ctro_salud = models.ForeignKey(CtroSalud, models.DO_NOTHING, db_column='id_ctro_salud', blank=True, null=True)
    id_prev = models.ForeignKey(Prevision, models.DO_NOTHING, db_column='id_prev', blank=True, null=True)
    id_patologia = models.ForeignKey(Patologia, models.DO_NOTHING, db_column='id_patologia', blank=True, null=True)
    id_tipo_paciente = models.ForeignKey('TipoPaciente', models.DO_NOTHING, db_column='id_tipo_paciente', blank=True, null=True)
    fech_defun = models.DateField(blank=True, null=True)

    def __str__(self):
            return self.rut_socio

    class Meta:
        managed = False
        db_table = 'socio'


class TipoPaciente(models.Model):
    id_tipo_pacientes = models.AutoField(primary_key=True)
    nom_tipo_pacientes = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
            return self.nom_tipo_pacientes

    class Meta:
        managed = False
        db_table = 'tipo_paciente'
        verbose_name_plural = "Tipos de Pacientes"
