# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fechaHora',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 22, 7, 956548), help_text=b'Fecha y hora del evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 3, 6, 10, 22, 7, 952491), help_text=b'Fecha que sera mostrada en la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 22, 7, 952534), help_text=b'Fecha y hora de inicio de la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
    ]
