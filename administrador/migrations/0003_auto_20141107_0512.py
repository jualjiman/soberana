# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20141107_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_fin',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_inicio',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
