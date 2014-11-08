# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asociaciones', '0004_auto_20141017_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'10')),
                ('asociacion', models.ForeignKey(blank=True, to='asociaciones.Asociacion', null=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Lineas',
                'permissions': (('detail_linea', 'Detalle De Linea'), ('rutas_linea', 'Rutas de Linea')),
            },
            bases=(models.Model,),
        ),
    ]
