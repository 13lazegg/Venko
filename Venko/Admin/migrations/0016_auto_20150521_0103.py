# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_auto_20150521_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='alumno',
            field=models.ForeignKey(blank=True, to='Admin.Alumno', null=True),
            preserve_default=True,
        ),
    ]
