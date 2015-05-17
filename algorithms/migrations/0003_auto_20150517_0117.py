# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import algorithms.models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0002_remove_algorithm_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='image',
            field=models.ImageField(null=True,default=None, upload_to=algorithms.models.upload_path_handler),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='algorithm',
            name='repository',
            field=models.CharField(null=True,default=None, max_length=255),
            preserve_default=False,
        ),
    ]
