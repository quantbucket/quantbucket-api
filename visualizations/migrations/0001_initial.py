# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('output', models.TextField()),
                ('analysis', models.ForeignKey(to='analysis.Analysis')),
            ],
        ),
        migrations.CreateModel(
            name='Visualization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.TextField()),
                ('version', models.CharField(max_length=255)),
                ('developer', models.ForeignKey(to='users.User')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='visualization',
            field=models.ManyToManyField(to='visualizations.Visualization'),
        ),
    ]
