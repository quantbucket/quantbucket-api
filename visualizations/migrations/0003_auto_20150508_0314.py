# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualizations', '0002_remove_visualization_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visualization',
            old_name='algorithm',
            new_name='algorithms',
        ),
    ]
