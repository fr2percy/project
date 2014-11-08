# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0006_auto_20141026_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zona',
            options={'ordering': ['nombre']},
        ),
        migrations.AddField(
            model_name='posicion',
            name='bajada',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posicion',
            name='subida',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calle',
            name='nombre',
            field=models.CharField(max_length=b'10', verbose_name='Nombre de Calle/Avenida'),
        ),
    ]
