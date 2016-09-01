# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shows',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
