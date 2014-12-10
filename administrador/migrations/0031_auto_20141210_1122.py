# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0030_auto_20141118_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicacion',
            options={'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 12, 10, 11, 22, 38, 720348), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 11, 22, 38, 720384), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='texto',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
