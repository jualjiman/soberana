# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_auto_20141109_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 9, 18, 17, 18, 860460)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 17, 18, 860504), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 17, 18, 860485)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='titulo',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
    ]
