# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaingreso', models.DateTimeField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('fechanacimiento', models.DateField()),
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
            name='Antecedente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deporte', models.CharField(max_length=15)),
                ('frecuencia', models.CharField(max_length=15)),
                ('plantillas', models.BooleanField(default=None)),
                ('dolores', models.CharField(max_length=50)),
                ('objetivos', models.CharField(max_length=140)),
                ('alumno', models.ForeignKey(to='Admin.Alumno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='antecedentes',
            name='alumno',
        ),
        migrations.DeleteModel(
            name='Antecedentes',
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='alumno',
            field=models.ForeignKey(to='Admin.Alumno'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Alumnos',
        ),
    ]
