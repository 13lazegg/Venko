# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20150207_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='apellido',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
    ]
