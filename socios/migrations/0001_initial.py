# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('id_socios', models.AutoField(primary_key=True, serialize=False)),
                ('cod_socios', models.CharField(blank=True, max_length=15, null=True)),
                ('rut_socios', models.CharField(blank=True, max_length=10, null=True)),
                ('sexo_socios', models.CharField(blank=True, max_length=1, null=True)),
                ('nom_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('apel_pat_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('apel_mat_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('dir_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('email_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('telef_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('cel_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('fech_nac_socios', models.DateField(blank=True, null=True)),
                ('foto_socios', models.CharField(blank=True, max_length=45, null=True)),
                ('region_numero', models.IntegerField(blank=True, null=True)),
                ('comuna_numero', models.IntegerField(blank=True, null=True)),
                ('fech_ing_socios', models.DateField(blank=True, null=True)),
                ('id_estado', models.IntegerField(blank=True, null=True)),
                ('id_est_civil', models.IntegerField(blank=True, null=True)),
                ('id_profesion', models.IntegerField(blank=True, null=True)),
                ('id_salud', models.IntegerField(blank=True, null=True)),
                ('id_ctro_salud', models.IntegerField(blank=True, null=True)),
                ('id_prev', models.IntegerField(blank=True, null=True)),
                ('id_perf', models.IntegerField(blank=True, null=True)),
                ('id_patologia', models.IntegerField(blank=True, null=True)),
                ('id_apoderado', models.IntegerField(blank=True, null=True)),
                ('id_tipo_paciente', models.IntegerField(blank=True, null=True)),
                ('fech_actu', models.DateTimeField(blank=True, null=True)),
                ('log_usuario', models.IntegerField(blank=True, null=True)),
                ('ciudad_numero', models.IntegerField(blank=True, null=True)),
                ('fech_defun', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'socios',
                'managed': False,
            },
        ),
    ]
