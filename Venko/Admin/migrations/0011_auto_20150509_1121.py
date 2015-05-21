# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_alumno_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagocuenta',
            name='fecha',
            field=models.DateField(default=datetime.date(2015, 5, 9)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagocuenta',
            name='pago',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
