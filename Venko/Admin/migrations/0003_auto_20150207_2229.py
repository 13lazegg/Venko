# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_auto_20150207_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fechaingreso',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
