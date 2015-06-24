# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_auto_20150307_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='slug',
            field=models.SlugField(default='blablabalbalabla', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(help_text=b'Descripcion del evento', max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaHora',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 23, 22, 41, 51, 509183), help_text=b'Fecha y hora del evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 6, 23, 22, 41, 51, 507095), help_text=b'Fecha que sera mostrada en la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 23, 22, 41, 51, 507119), help_text=b'Fecha y hora de inicio de la publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
    ]
