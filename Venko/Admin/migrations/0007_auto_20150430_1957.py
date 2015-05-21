# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_auto_20150421_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoServicio', models.CharField(max_length=40)),
                ('vecesPorSemana', models.IntegerField(max_length=1)),
                ('valor', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alumno',
            name='descuento',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alumno',
            name='servicio',
            field=models.ForeignKey(to='Admin.Servicio', null=True),
            preserve_default=True,
        ),
    ]
