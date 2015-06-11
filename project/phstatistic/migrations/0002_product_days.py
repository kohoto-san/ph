# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phstatistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='days',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
