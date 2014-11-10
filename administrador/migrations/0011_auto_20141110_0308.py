# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0010_auto_20141110_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 3, 8, 53, 332037), help_text=b'Fecha que sera mostrada en la noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(help_text=b'Fecha y hora de fin de publicacion del evento', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 3, 8, 53, 332061), help_text=b'Fecha y hora de inicio de publicacion del evento'),
            preserve_default=True,
        ),
    ]
