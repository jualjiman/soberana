# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0032_auto_20141219_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivopublicacion',
            name='publicacion',
            field=models.ForeignKey(default=1, to='administrador.Publicacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enlacepublicacion',
            name='publicacion',
            field=models.ForeignKey(default=1, to='administrador.Publicacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videopublicacion',
            name='publicacion',
            field=models.ForeignKey(default=1, to='administrador.Publicacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 12, 19, 11, 41, 18, 176287), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 11, 41, 18, 176323), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
