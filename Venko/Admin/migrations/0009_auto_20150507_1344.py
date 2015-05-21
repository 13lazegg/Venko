# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_pagocuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagocuenta',
            name='fecha',
            field=models.DateField(default=datetime.date(2015, 5, 7)),
            preserve_default=True,
        ),
    ]
