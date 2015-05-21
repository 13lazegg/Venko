# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20150430_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoCuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date(2015, 5, 4))),
                ('pago', models.FloatField()),
                ('alumno', models.ForeignKey(to='Admin.Alumno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
