# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_proile_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proile',
            new_name='profile',
        ),
    ]
