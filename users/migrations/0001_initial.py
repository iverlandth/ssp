# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=12, unique=True, verbose_name='CI')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Apellido paterno')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido materno')),
                ('gender', models.CharField(choices=[('F', 'FEMENINO'), ('M', 'MASCULINO')], max_length=2, verbose_name='G\xe9nero')),
                ('date_of_birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('marital_status', models.CharField(choices=[('SO', 'SOLTERO(A)'), ('CA', 'CASADO(A)'), ('VI', 'VIUDO(A)'), ('DI', 'DIVORCIADO(A)'), ('CO', 'CONCUBINO(A)'), ('SE', 'SEPARADO(A)'), ('FA', 'FALLECIDO(A)')], max_length=2, verbose_name='Estado Civil')),
                ('home_address', models.CharField(max_length=100, verbose_name='Direcci\xf3n')),
                ('mobile_phone', models.CharField(blank=True, max_length=25, verbose_name='Nro. de Celular')),
                ('rol', models.CharField(choices=[('SUP', 'SUPERVISER'), ('TEC', 'TECNICO')], default='TEC', max_length=3, verbose_name='Rol')),
                ('imei_code', models.CharField(blank=True, max_length=25, verbose_name='Imei Celular')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]