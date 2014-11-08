# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0002_posicion'),
    ]

    operations = [
        migrations.AddField(
            model_name='posicion',
            name='inicio',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
