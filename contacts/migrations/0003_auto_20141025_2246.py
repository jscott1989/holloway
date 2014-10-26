# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='contacts',
            field=models.ManyToManyField(related_name='groups', to='contacts.Contact'),
            preserve_default=True,
        ),
    ]
