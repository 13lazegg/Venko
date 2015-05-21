# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_auto_20150521_0025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CajaDiaria',
        ),
        migrations.AlterField(
            model_name='pagocuenta',
            name='alumno',
            field=models.ForeignKey(default=None, to='Admin.Alumno'),
            preserve_default=True,
        ),
    ]
