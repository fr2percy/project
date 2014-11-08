# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asociacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'30')),
                ('direccion', models.CharField(max_length=b'100')),
                ('telefono', models.CharField(max_length=b'10')),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
            options={
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
    ]
