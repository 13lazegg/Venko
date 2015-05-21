# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_auto_20150323_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='peso',
            field=models.IntegerField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
