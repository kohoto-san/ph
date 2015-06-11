# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('votes_count', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.CharField(max_length=255)),
                ('discussion_url', models.CharField(max_length=255)),
                ('redirect_url', models.CharField(max_length=255)),
                ('created_at', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
