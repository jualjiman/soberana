# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_auto_20141107_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to=b'eventos')),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('link', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('pdf', models.FileField(upload_to=b'pdfevento', blank=True)),
                ('fecha', models.DateField(default=datetime.datetime(2014, 11, 9, 16, 37, 31, 713226))),
                ('fecha_inicio', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 16, 37, 31, 713249))),
                ('fecha_fin', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 16, 37, 31, 713266), blank=True)),
                ('categoria', models.CharField(max_length=2, choices=[(b'SV', 'Siempre visible'), (b'NL', 'Normal')])),
                ('orden', models.IntegerField(default=100)),
                ('activo', models.BooleanField(default=True)),
                ('permanente', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Noticia',
        ),
    ]
