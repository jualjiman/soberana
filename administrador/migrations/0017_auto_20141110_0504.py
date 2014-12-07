# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0016_auto_20141110_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='descripcionVideoYoutube',
            field=models.CharField(default='', help_text=b'Texto descriptivo del video de youtube.', max_length=60, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 5, 4, 32, 585540), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 5, 4, 32, 585564), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
