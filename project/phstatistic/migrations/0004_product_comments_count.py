# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phstatistic', '0003_auto_20150609_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comments_count',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
    ]
