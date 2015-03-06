# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_auto_20150306_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='fechaHoraFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 30, 26, 217574), help_text=b'Fecha y hora de fin del evento', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evento',
            name='textoLink',
            field=models.CharField(default='', help_text=b'Texto del link', max_length=300, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaHora',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 30, 26, 217535), help_text=b'Fecha y hora del evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 3, 6, 10, 30, 26, 212665), help_text=b'Fecha que sera mostrada en la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 10, 30, 26, 212732), help_text=b'Fecha y hora de inicio de la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
    ]
