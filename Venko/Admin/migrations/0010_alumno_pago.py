# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_auto_20150507_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='pago',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
