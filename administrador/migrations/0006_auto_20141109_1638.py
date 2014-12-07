# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_auto_20141109_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 9, 16, 38, 14, 254342)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 16, 38, 14, 254384), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 16, 38, 14, 254366)),
            preserve_default=True,
        ),
    ]
