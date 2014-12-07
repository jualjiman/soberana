# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 7, 4, 44, 15, 902286)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 4, 44, 15, 902327), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 4, 44, 15, 902309)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='pdf',
            field=models.FileField(upload_to=b'pdfnoticias', blank=True),
            preserve_default=True,
        ),
    ]
