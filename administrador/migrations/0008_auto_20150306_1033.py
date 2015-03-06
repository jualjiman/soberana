# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_auto_20150306_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fechaHora',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 33, 47, 110398), help_text=b'Fecha y hora del evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaHoraFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 33, 47, 110451), help_text=b'Fecha y hora de fin del evento', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 3, 6, 10, 33, 47, 105491), help_text=b'Fecha que sera mostrada en la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 33, 47, 105564), help_text=b'Fecha y hora de inicio de la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
    ]
