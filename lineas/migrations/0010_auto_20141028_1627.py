# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0009_auto_20141028_1618'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posicion_Zona',
            new_name='Posicion_Calle',
        ),
    ]
