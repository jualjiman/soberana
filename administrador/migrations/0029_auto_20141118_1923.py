# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrador', '0028_auto_20141111_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='creator',
            field=models.ForeignKey(related_name='CreadorPublicacion', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='activo',
            field=models.BooleanField(default=False, help_text=b'Debera ser mostrado?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 18, 19, 23, 17, 320010), help_text=b'Fecha a partir de la cual sera mostrada la publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 18, 19, 23, 17, 320045), help_text=b'Fecha y hora de inicio de la publicacion'),
            preserve_default=True,
        ),
    ]
