from django.forms import ModelForm
from models import EmailTemplate

class EmailTemplateForm(ModelForm):
    class Meta:
        model = EmailTemplate
        fields = ("subject", "html", "text", "required_fields")
