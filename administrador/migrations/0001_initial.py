# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionArchivo', models.CharField(help_text=b'Texto descriptivo del archivo.', max_length=60)),
                ('archivo', models.FileField(help_text=b'Archivo asociado con la publicacion', upload_to=b'pdfpublicacion')),
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
                ('descripcionLink', models.CharField(help_text=b'Texto descriptivo del link.', max_length=60)),
                ('link', models.URLField(help_text=b'Link asociado con la publicacion')),
            ],
            options={
                'verbose_name_plural': 'Enlaces de publicaci\xf3n',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activo', models.BooleanField(default=False, help_text=b'Debera ser mostrado?')),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to=b'publicaciones')),
                ('titulo', models.CharField(help_text=b'Titulo de la publicacion', max_length=60)),
                ('resumen', models.CharField(help_text=b'Rese\xc3\xb1a de la publicacion que sera mostrada (150 caracteres)', max_length=150)),
                ('texto', ckeditor.fields.RichTextField()),
                ('fecha', models.DateField(default=datetime.datetime(2015, 2, 20, 13, 33, 13, 463094), help_text=b'Fecha que sera mostrada en la publicaci\xc3\xb3n')),
                ('fecha_inicio', models.DateTimeField(default=datetime.datetime(2015, 2, 20, 13, 33, 13, 463138), help_text=b'Fecha y hora de inicio de la publicaci\xc3\xb3n')),
                ('fecha_fin', models.DateTimeField(help_text=b'Fecha y hora en que dejara de ser mostrada la publicaci\xc3\xb3n. Si se deja en blanco sera permanente', null=True, blank=True)),
                ('categoria', models.IntegerField(help_text=b'Define la prioridad de la publicaci\xc3\xb3n', choices=[(1, 'Importante'), (0, 'Normal')])),
                ('creator', models.ForeignKey(related_name='CreadorPublicacion', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('editer', models.ForeignKey(related_name='ModificoPublicacion', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Publicaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to=b'sliders')),
                ('titulo', models.CharField(help_text=b'Titulo que aparecera en el recuadro rojo', max_length=60, blank=True)),
                ('link', models.CharField(help_text=b'Link al que enviara el slide', max_length=300, blank=True)),
                ('orden', models.IntegerField(default=100, help_text=b'Numeros mayores van primero')),
                ('activo', models.BooleanField(default=True, help_text=b'Debera ser mostrado?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionVideoYoutube', models.CharField(help_text=b'Texto descriptivo del video de youtube.', max_length=60)),
                ('claveYoutube', models.CharField(help_text=b'Clave de video de youtube asociado con la publicacion', max_length=20)),
                ('publicacion', models.ForeignKey(to='administrador.Publicacion')),
            ],
            options={
                'verbose_name_plural': 'Videos de publicacion',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='enlacepublicacion',
            name='publicacion',
            field=models.ForeignKey(to='administrador.Publicacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archivopublicacion',
            name='publicacion',
            field=models.ForeignKey(to='administrador.Publicacion'),
            preserve_default=True,
        ),
    ]
