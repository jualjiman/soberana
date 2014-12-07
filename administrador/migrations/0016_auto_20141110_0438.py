# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0015_auto_20141110_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='descripcionLink',
            field=models.CharField(default='', help_text=b'Texto descriptivo del link.', max_length=60, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='descripcionPdf',
            field=models.CharField(default='', help_text=b'Texto descriptivo del PDF.', max_length=60, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 4, 37, 59, 704781), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 4, 37, 59, 704804), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
