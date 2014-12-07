# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20141107_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 7, 5, 15, 39, 431127)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 5, 15, 39, 431167), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 5, 15, 39, 431151)),
            preserve_default=True,
        ),
    ]
