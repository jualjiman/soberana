# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0031_auto_20141210_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionArchivo', models.CharField(help_text=b'Texto descriptivo del archivo.', max_length=60, blank=True)),
                ('archivo', models.FileField(help_text=b'Archivo asociado con la publicacion', upload_to=b'pdfpublicacion', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Archivo de publicaci\xf3n',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EnlacePublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionLink', models.CharField(help_text=b'Texto descriptivo del link.', max_length=60, blank=True)),
                ('link', models.URLField(help_text=b'Link asociado con la publicacion', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Enlaces de publicaci\xf3n',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionVideoYoutube', models.CharField(help_text=b'Texto descriptivo del video de youtube.', max_length=60, blank=True)),
                ('claveYoutube', models.CharField(help_text=b'Clave de video de youtube asociado con la publicacion', max_length=20, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Videos de publicacion',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 12, 19, 11, 36, 58, 421637), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 11, 36, 58, 421673), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
