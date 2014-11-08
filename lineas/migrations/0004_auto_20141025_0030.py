# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0003_posicion_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posicion',
            name='latitud',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='longitud',
            field=models.CharField(max_length=50),
        ),
    ]
