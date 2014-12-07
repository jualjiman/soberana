# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0027_auto_20141111_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.IntegerField(help_text=b'Define la prioridad de la publicacion', choices=[(1, 'Importante'), (0, 'Normal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 11, 22, 53, 19, 877200), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 22, 53, 19, 877247), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
