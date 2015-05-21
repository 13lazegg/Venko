# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_auto_20150509_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='deporte',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='derivadopor',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='descuento',
            field=models.IntegerField(default=0, max_length=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='direccion',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='email',
            field=models.CharField(max_length=35, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='fechanacimiento',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='medicacion',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='medicotratante',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=80, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='obrasocial',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='peso',
            field=models.IntegerField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='profesion',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='talla',
            field=models.IntegerField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=17, blank=True),
            preserve_default=True,
        ),
    ]
