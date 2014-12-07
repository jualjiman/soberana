# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0017_auto_20141110_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='youtube',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='codigoVideoYoutube',
            field=models.URLField(default='', help_text=b'Codigo del video de youtube asociado con la publicacion', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 5, 8, 44, 874790), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 5, 8, 44, 874814), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
