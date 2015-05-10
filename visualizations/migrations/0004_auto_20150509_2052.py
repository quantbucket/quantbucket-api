# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0002_remove_algorithm_module'),
        ('visualizations', '0003_auto_20150508_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualizationMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visualization_field', models.CharField(max_length=255)),
                ('algorithm_field', models.CharField(max_length=255)),
                ('algorithm', models.ForeignKey(to='algorithms.Algorithm')),
            ],
        ),
        migrations.AddField(
            model_name='visualization',
            name='arch',
            field=models.CharField(default='backend', max_length=10, choices=[(b'frontend', b'frontend'), (b'backend', b'backend')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visualizationmapping',
            name='visualization',
            field=models.ForeignKey(to='visualizations.Visualization'),
        ),
    ]
