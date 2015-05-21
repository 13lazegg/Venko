# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_auto_20150421_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='talla',
            field=models.IntegerField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
