# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160830_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='eyy@gmail.com'),
            preserve_default=False,
        ),
    ]
