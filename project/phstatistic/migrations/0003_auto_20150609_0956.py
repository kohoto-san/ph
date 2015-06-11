# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phstatistic', '0002_product_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='days',
            new_name='day',
        ),
    ]
