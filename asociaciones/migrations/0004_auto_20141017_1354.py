# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asociaciones', '0003_auto_20141017_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asociacion',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Asociaciones', 'permissions': (('detail_asociacion', 'Detalle de Asociacion'), ('report_asociacion', 'Reporte de Asociacion'), ('mi_asociacion', 'Permisos Asociacion '))},
        ),
        migrations.AddField(
            model_name='asociacion',
            name='usuario',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
