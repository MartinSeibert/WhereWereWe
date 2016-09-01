# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='asdf'),
            preserve_default=False,
        ),
    ]
