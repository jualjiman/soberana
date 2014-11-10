# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0019_auto_20141110_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='videoYoutube',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='claveYoutube',
            field=models.CharField(default='', help_text=b'Clave de video de youtube asociado con la publicacion', max_length=20, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 10, 5, 25, 31, 541422), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 5, 25, 31, 541445), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
