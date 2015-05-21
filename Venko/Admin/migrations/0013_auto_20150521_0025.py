# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_auto_20150509_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='CajaDiaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date(2015, 5, 21))),
                ('pago', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alumno',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='servicio',
            field=models.ForeignKey(to='Admin.Servicio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagocuenta',
            name='fecha',
            field=models.DateField(default=datetime.date(2015, 5, 21)),
            preserve_default=True,
        ),
    ]
