# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='activo',
            field=models.BooleanField(default=True, help_text=b'Debera ser mostrado?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slider',
            name='link',
            field=models.CharField(default='', help_text=b'Link al que enviara el slide', max_length=300, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 2, 10, 11, 36, 31, 854228), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 10, 11, 36, 31, 854265), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
