# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_episode'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='eps',
            field=models.ManyToManyField(to='main.Episode'),
            preserve_default=True,
        ),
    ]
