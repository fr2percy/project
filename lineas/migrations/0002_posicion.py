# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('linea', models.ForeignKey(blank=True, to='lineas.Linea', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
