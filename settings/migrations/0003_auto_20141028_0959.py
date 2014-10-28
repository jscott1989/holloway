# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20141028_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='default_from_address',
            field=encrypted_fields.fields.EncryptedEmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtp_host',
            field=encrypted_fields.fields.EncryptedCharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtp_password',
            field=encrypted_fields.fields.EncryptedCharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtp_username',
            field=encrypted_fields.fields.EncryptedCharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
