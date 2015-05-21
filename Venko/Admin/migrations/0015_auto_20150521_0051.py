# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_auto_20150521_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date(2015, 5, 21))),
                ('pago', models.IntegerField()),
                ('alumno', models.ForeignKey(default=None, to='Admin.Alumno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pagocuenta',
            name='alumno',
        ),
        migrations.DeleteModel(
            name='PagoCuenta',
        ),
    ]
