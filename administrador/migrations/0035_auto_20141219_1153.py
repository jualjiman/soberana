# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0034_auto_20141219_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='claveYoutube',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='descripcionLink',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='descripcionPdf',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='descripcionVideoYoutube',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='link',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='pdf',
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 12, 19, 11, 53, 49, 542973), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 11, 53, 49, 543007), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
