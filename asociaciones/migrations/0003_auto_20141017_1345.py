# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asociaciones', '0002_auto_20141017_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociacion',
            name='email',
            field=models.EmailField(unique=True, max_length=75, verbose_name=b'Correo Electronico'),
        ),
    ]
