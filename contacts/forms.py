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