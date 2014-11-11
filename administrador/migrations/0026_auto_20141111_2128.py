# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0025_auto_20141111_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.IntegerField(help_text=b'Define la prioridad de la publicacion', choices=[(b'2', 'Muy importante'), (b'1', 'Importante'), (b'0', 'Normal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 11, 21, 28, 1, 451264), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 21, 28, 1, 451297), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
