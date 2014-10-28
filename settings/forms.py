from django import forms
from django.forms import ModelForm
from models import Settings

class SettingsForm(ModelForm):
    class Meta:
        model = Settings
        fields = ("default_from_address", "smtp_host", "smtp_port", "smtp_username", "smtp_password")

    smtp_host = forms.CharField(max_length=100, label="SMTP Host", required=False)
    smtp_port = forms.IntegerField(label="SMTP Port", required=False)
    smtp_username = forms.CharField(max_length=100, label="SMTP Username", required=False)
    smtp_password = forms.CharField(max_length=100, label="SMTP Password", required=False)