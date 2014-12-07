# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0024_auto_20141111_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='orden',
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.CharField(help_text=b'Define la prioridad de la publicacion', max_length=2, choices=[(b'MI', 'Muy importante'), (b'IM', 'Importante'), (b'NO', 'Normal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 11, 21, 7, 50, 779401), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 21, 7, 50, 779437), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
