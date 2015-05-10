# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import analysis.models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0004_auto_20150509_2052'),
        ('analysis', '0002_analysis_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisVisualization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=analysis.models.upload_path_handler)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('analysis', models.ForeignKey(to='analysis.Analysis')),
                ('visualization', models.ForeignKey(to='visualizations.Visualization')),
            ],
        ),
    ]
