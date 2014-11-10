# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_auto_20141109_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 2, 20, 51, 221374), help_text=b'Fecha que sera mostrada en la noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 2, 20, 51, 221425), help_text=b'Fecha y hora de fin de publicacion del evento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(help_text=b'Fecha y hora de inicio de publicacion del evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='resumen',
            field=models.CharField(help_text=b'Rese\xc3\xb1a de la noticia que sera mostrada (150 caracteres)', max_length=150),
            preserve_default=True,
        ),
    ]
