# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import encrypted_fields.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', encrypted_fields.fields.EncryptedEmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('html', models.TextField()),
                ('text', models.TextField()),
                ('required_fields', jsonfield.fields.JSONField(default=dict)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SMTPAccount',
            fields=[
                ('account_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='emails.Account')),
                ('smtp_host', encrypted_fields.fields.EncryptedCharField(max_length=100, null=True)),
                ('smtp_port', models.IntegerField(null=True)),
                ('smtp_username', encrypted_fields.fields.EncryptedCharField(max_length=100, null=True)),
                ('smtp_password', encrypted_fields.fields.EncryptedCharField(max_length=100, null=True)),
            ],
            options={
            },
            bases=('emails.account',),
        ),
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
