# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaingreso', models.DateTimeField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('fechanacimiento', models.DateTimeField()),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=17)),
                ('email', models.CharField(max_length=35)),
                ('obrasocial', models.CharField(max_length=40)),
                ('profesion', models.CharField(max_length=50)),
                ('deporte', models.CharField(max_length=25)),
                ('medicotratante', models.CharField(max_length=25)),
                ('derivadopor', models.CharField(max_length=25)),
                ('medicacion', models.CharField(max_length=140)),
                ('peso', models.IntegerField(max_length=10)),
                ('talla', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deporte', models.CharField(max_length=15)),
                ('frecuencia', models.CharField(max_length=15)),
                ('plantillas', models.BooleanField(default=None)),
                ('dolores', models.CharField(max_length=50)),
                ('objetivos', models.CharField(max_length=140)),
                ('alumno', models.ForeignKey(to='Admin.Alumnos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diagnostico', models.CharField(max_length=250)),
                ('estadoactual', models.CharField(max_length=250)),
                ('tiempoevolucion', models.CharField(max_length=140)),
                ('tratamientoactual', models.CharField(max_length=140)),
                ('anteriores', models.CharField(max_length=140)),
                ('mecanismoaccion', models.CharField(max_length=140)),
                ('estudioscomplementarios', models.CharField(max_length=140)),
                ('antecedentesconsideracion', models.CharField(max_length=140)),
                ('ta', models.IntegerField(max_length=5)),
                ('fc', models.CharField(max_length=5)),
                ('hta', models.CharField(max_length=5)),
                ('dbt', models.BooleanField(default=None)),
                ('dislipemias', models.BooleanField(default=None)),
                ('tabaco', models.BooleanField(default=None)),
                ('arritmias', models.BooleanField(default=None)),
                ('desmayos', models.BooleanField(default=None)),
                ('tiroides', models.BooleanField(default=None)),
                ('alumno', models.ForeignKey(to='Admin.Alumnos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
