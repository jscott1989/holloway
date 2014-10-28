# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='smtp_host',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtp_password',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtp_port',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtp_username',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
