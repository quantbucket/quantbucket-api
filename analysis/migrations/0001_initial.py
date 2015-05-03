# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0001_initial'),
        ('algorithms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('algorithm', models.ForeignKey(to='algorithms.Algorithm')),
                ('dataset', models.ForeignKey(to='datasets.Dataset')),
            ],
        ),
    ]
