from django.db import models
from django.contrib.auth.models import User
from encrypted_fields import EncryptedCharField, EncryptedEmailField

class Settings(models.Model):
    owner = models.OneToOneField("auth.User", primary_key=True)

    default_from_address = EncryptedEmailField()

    smtp_host = EncryptedCharField(max_length=100, null=True)
    smtp_port = models.IntegerField(null=True)
    smtp_username = EncryptedCharField(max_length=100, null=True)
    smtp_password = EncryptedCharField(max_length=100, null=True)


def get_user_owner(self):
    return None
User.owner = property(get_user_owner)