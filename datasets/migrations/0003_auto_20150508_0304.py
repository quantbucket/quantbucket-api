# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datasets.models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0002_auto_20150507_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='data',
            field=models.FileField(upload_to=datasets.models.upload_path_handler),
        ),
    ]
