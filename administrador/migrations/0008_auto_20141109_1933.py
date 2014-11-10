# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_auto_20141109_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='resumen',
            field=models.CharField(default='', help_text=b'Rese\xc3\xb1a de la noticia que sera mostrada', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='activo',
            field=models.BooleanField(default=True, help_text=b'Debera ser mostrado?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='categoria',
            field=models.CharField(help_text=b'Define la prioridad de la publicacion', max_length=2, choices=[(b'SV', 'Siempre visible'), (b'NL', 'Normal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(help_text=b'Texto correspondiente al evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 9, 19, 32, 49, 851911), help_text=b'Fecha que sera mostrada en la noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 19, 32, 49, 851954), help_text=b'Fecha y hora de fin de publicacion del evento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 19, 32, 49, 851937), help_text=b'Fecha y hora de inicio de publicacion del evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='link',
            field=models.URLField(help_text=b'Link asociado con la informacion', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='orden',
            field=models.IntegerField(default=100, help_text=b'Numeros mayores van primero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='pdf',
            field=models.FileField(help_text=b'Archivo pdf asociado con la informacion', upload_to=b'pdfevento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='permanente',
            field=models.BooleanField(default=False, help_text=b'Indica que la noticia no debera ser retirada'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(help_text=b'Titulo del evento', max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='youtube',
            field=models.URLField(help_text=b'Link de video de youtube asociado con la informacion|', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='activo',
            field=models.BooleanField(default=True, help_text=b'Debera ser mostrado?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='orden',
            field=models.IntegerField(default=100, help_text=b'Numeros mayores van primero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='titulo',
            field=models.CharField(help_text=b'Titulo que aparecera en el recuadro rojo', max_length=60, blank=True),
            preserve_default=True,
        ),
    ]
