# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('owner', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('default_from_address', models.EmailField(max_length=75)),
                ('smtp_host', models.CharField(max_length=100)),
                ('smtp_port', models.IntegerField()),
                ('smtp_username', models.CharField(max_length=100)),
                ('smtp_password', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
