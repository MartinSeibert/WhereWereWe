# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_show_episodes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='eps',
            new_name='episodes',
        ),
    ]
