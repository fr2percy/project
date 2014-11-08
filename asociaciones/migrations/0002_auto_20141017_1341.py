# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asociaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asociacion',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Asociaciones', 'permissions': (('detail_asociacion', 'Detalle de Asociacion'), ('report_asociacion', 'Reporte de Asociacion'))},
        ),
        migrations.AddField(
            model_name='asociacion',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=75, verbose_name=b'Correo Electronico'),
            preserve_default=False,
        ),
    ]
