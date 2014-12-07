# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0012_auto_20141110_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to=b'publicaciones')),
                ('titulo', models.CharField(help_text=b'Titulo de la publicacion', max_length=60)),
                ('resumen', models.CharField(help_text=b'Rese\xc3\xb1a de la publicacion que sera mostrada (150 caracteres)', max_length=150)),
                ('descripcion', models.TextField(help_text=b'Texto correspondiente a la publicacion')),
                ('link', models.URLField(help_text=b'Link asociado con la publicacion', blank=True)),
                ('youtube', models.URLField(help_text=b'Link de video de youtube asociado con la publicacion', blank=True)),
                ('pdf', models.FileField(help_text=b'Archivo pdf asociado con la publicacion', upload_to=b'pdfpublicacion', blank=True)),
                ('fecha', models.DateField(default=datetime.datetime(2014, 11, 10, 3, 23, 7, 305888), help_text=b'Fecha a partir de la cual sera mostrada la publicacion')),
                ('fecha_inicio', models.DateTimeField(default=datetime.datetime(2014, 11, 10, 3, 23, 7, 305914), help_text=b'Fecha y hora de inicio de la publicacion')),
                ('fecha_fin', models.DateTimeField(help_text=b'Fecha y hora en que dejara de ser mostrada la publicacion. Si se deja en blanco sera permanente', null=True, blank=True)),
                ('categoria', models.CharField(help_text=b'Define la prioridad de la publicacion', max_length=2, choices=[(b'SV', 'Siempre visible'), (b'NL', 'Normal')])),
                ('orden', models.IntegerField(default=100, help_text=b'Numeros mayores van primero')),
                ('activo', models.BooleanField(default=True, help_text=b'Debera ser mostrado?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
    ]
