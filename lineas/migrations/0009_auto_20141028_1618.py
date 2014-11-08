# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0008_posicion_zona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calle',
            name='nombre',
            field=models.CharField(max_length=b'30', verbose_name='Nombre de Calle/Avenida'),
        ),
        migrations.AlterField(
            model_name='zona',
            name='nombre',
            field=models.CharField(unique=True, max_length=b'20'),
        ),
    ]
