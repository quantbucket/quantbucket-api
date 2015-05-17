# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_analysisvisualization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisvisualization',
            name='analysis',
            field=models.ForeignKey(related_name='visualizations', to='analysis.Analysis'),
        ),
    ]
