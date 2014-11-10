# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0020_auto_20141110_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 15, 53, 34, 535535), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 15, 53, 34, 535576), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
