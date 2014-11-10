# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to=b'noticias')),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('pdf', models.FileField(upload_to=b'pdfnoticias')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2014, 11, 7, 4, 33, 13, 350176))),
                ('fecha_inicio', models.DateTimeField(default=datetime.datetime(2014, 11, 7, 4, 33, 13, 350199))),
                ('fecha_fin', models.DateTimeField(default=datetime.datetime(2014, 11, 7, 4, 33, 13, 350215))),
                ('categoria', models.CharField(max_length=2, choices=[(b'SV', 'Siempre visible'), (b'NL', 'Normal')])),
                ('orden', models.IntegerField(default=100)),
                ('activo', models.BooleanField(default=True)),
                ('permanente', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to=b'sliders')),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=70, blank=True)),
                ('orden', models.IntegerField(default=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
