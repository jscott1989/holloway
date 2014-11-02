from django import forms
from django.forms import ModelForm
from models import Contact, Group

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email", "fields")

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ("name", "description")

class ImportUploadForm(forms.Form):
    file = forms.FileField(label='Select a CSV file')