# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0007_auto_20141026_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posicion_Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle', models.ForeignKey(to='lineas.Calle')),
                ('posicion', models.ForeignKey(to='lineas.Posicion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
