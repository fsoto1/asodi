# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.forms import ModelForm


class Apoderado(models.Model):
    id_apoderado = models.AutoField(primary_key=True)
    cod_apoderado = models.CharField(max_length=15, blank=True, null=True)
    rut_apoderado = models.CharField(max_length=10, blank=True, null=True)
    nom_apoderado = models.CharField(max_length=45, blank=True, null=True)
    apel_pat_apoderado = models.CharField(max_length=45, blank=True, null=True)
    apel_mat_apoderado = models.CharField(max_length=45, blank=True, null=True)
    email_apoderado = models.CharField(max_length=45, blank=True, null=True)
    telef_apoderado = models.CharField(max_length=45, blank=True, null=True)
    fech_nac_apoderado = models.DateField(blank=True, null=True)
    foto_apoderado = models.CharField(max_length=45, blank=True, null=True)
    comuna_numero = models.IntegerField(blank=True, null=True)
    dir_apoderado = models.CharField(max_length=45, blank=True, null=True)
    fech_ing_apod = models.DateField(blank=True, null=True)
    id_socio = models.IntegerField(blank=True, null=True)
    fech_act_apod = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apoderado'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BloqueosTomaHoras(models.Model):
    id_bloqueo = models.AutoField(primary_key=True)
    desde = models.DateTimeField()
    hasta = models.DateTimeField()
    tratante = models.IntegerField()
    comentario = models.TextField()

    class Meta:
        managed = False
        db_table = 'bloqueos_toma_horas'


class CitacionTemp(models.Model):
    txt1 = models.TextField()
    txt2 = models.TextField()
    txt3 = models.TextField()
    txt4 = models.TextField()

    class Meta:
        managed = False
        db_table = 'citacion_temp'


class Ciudad(models.Model):
    ciu_cod = models.IntegerField(primary_key=True)
    reg_cod = models.IntegerField()
    ciu_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comunas(models.Model):
    com_cod = models.AutoField(primary_key=True)
    reg_cod = models.IntegerField()
    com_nom = models.TextField()

    class Meta:
        managed = False
        db_table = 'comunas'


class CtroSalud(models.Model):
    id_ctro_salud = models.IntegerField(primary_key=True)
    nom_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    dir_ctro_salud = models.CharField(max_length=60, blank=True, null=True)
    rut_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    comuna_numero = models.IntegerField(blank=True, null=True)
    telef_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    email_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    med_ctro_salud = models.CharField(max_length=45, blank=True, null=True)
    enf_ctro_salud = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctro_salud'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Especialidad(models.Model):
    id_especialidad = models.IntegerField(primary_key=True)
    nom_especialidad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Especialista(models.Model):
    id_especialista = models.IntegerField(primary_key=True)
    nom_especialista = models.CharField(max_length=45, blank=True, null=True)
    apel_pat_especialista = models.CharField(max_length=45, blank=True, null=True)
    apel_mat_especialista = models.CharField(max_length=45, blank=True, null=True)
    email_especialista = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialista'


class EstCivil(models.Model):
    id_est_civil = models.AutoField(primary_key=True)
    nom_est_civil = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'est_civil'


class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nom_estado = models.CharField(max_length=45)
    com_estado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class LogMovSocios(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_usuario = models.IntegerField(blank=True, null=True)
    log_fecha = models.DateField(blank=True, null=True)
    log_id_socios = models.IntegerField()
    log_cod_socios = models.CharField(max_length=15, blank=True, null=True)
    log_rut_socios = models.CharField(max_length=10, blank=True, null=True)
    log_sexo_socios = models.CharField(max_length=1, blank=True, null=True)
    log_nom_socios = models.CharField(max_length=45, blank=True, null=True)
    log_apel_pat_socios = models.CharField(max_length=45, blank=True, null=True)
    log_apel_mat_socios = models.CharField(max_length=45, blank=True, null=True)
    log_dir_socios = models.CharField(max_length=45, blank=True, null=True)
    log_email_socios = models.CharField(max_length=45, blank=True, null=True)
    log_telef_socios = models.CharField(max_length=45, blank=True, null=True)
    log_cel_socios = models.CharField(max_length=45, blank=True, null=True)
    log_fech_nac_socios = models.DateField(blank=True, null=True)
    log_foto_socios = models.CharField(max_length=45, blank=True, null=True)
    log_region_numero = models.IntegerField(blank=True, null=True)
    log_ciudad_numero = models.IntegerField(blank=True, null=True)
    log_comuna_numero = models.IntegerField(blank=True, null=True)
    log_fech_ing_socios = models.DateField(blank=True, null=True)
    log_id_estado = models.IntegerField(blank=True, null=True)
    log_id_est_civil = models.IntegerField(blank=True, null=True)
    log_id_profesion = models.IntegerField(blank=True, null=True)
    log_id_salud = models.IntegerField(blank=True, null=True)
    log_id_ctro_salud = models.IntegerField(blank=True, null=True)
    log_id_prev = models.IntegerField(blank=True, null=True)
    log_id_perf = models.IntegerField(blank=True, null=True)
    log_id_patologia = models.IntegerField(blank=True, null=True)
    log_id_apoderado = models.IntegerField(blank=True, null=True)
    log_id_tipo_paciente = models.IntegerField(blank=True, null=True)
    log_fech_actu = models.DateField(blank=True, null=True)
    log_usuario_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_mov_socios'


class MovSocio(models.Model):
    mov_id = models.AutoField(primary_key=True)
    mov_id_tipo = models.IntegerField()
    mov_tipo = models.CharField(max_length=50)
    mov_fecha = models.DateField()
    mov_rut_socio = models.CharField(max_length=12)
    mov_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mov_socio'


class Patologia(models.Model):
    id_patologia = models.IntegerField(primary_key=True)
    nom_patologia = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'patologia'


class Perfiles(models.Model):
    id_perf = models.IntegerField(primary_key=True)
    nom_perf = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'perfiles'


class Perfpriv(models.Model):
    id_perf = models.IntegerField()
    id_priv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'perfpriv'


class Permisos(models.Model):
    id_perm = models.AutoField(primary_key=True)
    menu_perm = models.TextField()

    class Meta:
        managed = False
        db_table = 'permisos'


class Prevision(models.Model):
    id_prevision = models.IntegerField(primary_key=True)
    nom_prevision = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prevision'


class Privilegios(models.Model):
    id_priv = models.IntegerField(primary_key=True)
    nom_priv = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'privilegios'


class Profesion(models.Model):
    id_profesion = models.IntegerField(primary_key=True)
    nom_profesion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesion'


class Regiones(models.Model):
    region_numero = models.IntegerField(primary_key=True)
    nombre_region = models.TextField()

    class Meta:
        managed = False
        db_table = 'regiones'


class Salud(models.Model):
    id_salud = models.IntegerField(primary_key=True)
    nom_salud = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salud'


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

    class Meta:
        managed = False
        db_table = 'socios'


class TipoPacientes(models.Model):
    id_tipo_pacientes = models.IntegerField(primary_key=True)
    nom_tipo_pacientes = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_pacientes'


class TomaHoras(models.Model):
    id_toma_horas = models.AutoField(primary_key=True)
    id_socios = models.IntegerField(blank=True, null=True)
    fecha_toma_horas = models.DateField(blank=True, null=True)
    hora_toma_hora = models.CharField(max_length=100)
    id_usuario = models.IntegerField(blank=True, null=True)
    com_toma_horas = models.CharField(max_length=200, blank=True, null=True)
    id_centro = models.IntegerField(blank=True, null=True)
    id_especialista = models.IntegerField(blank=True, null=True)
    estado_hora = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'toma_horas'


class Usuarios(models.Model):
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    id_perfil = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
