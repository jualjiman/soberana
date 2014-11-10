# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0014_auto_20141110_0323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='descripcion',
            new_name='texto',
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 4, 28, 2, 589941), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 4, 28, 2, 589965), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
