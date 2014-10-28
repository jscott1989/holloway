from django import forms
from django.forms import ModelForm
from models import EmailTemplate
from contacts.models import Contact, Group

class EmailTemplateForm(ModelForm):
    class Meta:
        model = EmailTemplate
        fields = ("subject", "html", "text", "required_fields")

class EmailForm(forms.Form):
    to_addresses = forms.CharField(label="To")
    from_address = forms.EmailField(label="From")
    subject = forms.CharField(max_length=100)
    html = forms.CharField()
    text = forms.CharField()

    @property
    def contacts(self):
        """ Get a list of contacts the email should be sent to. """
        # This will resolve groups, and email addresses into contacts

        # TODO: Deal with addresses which don't have a contact - for now we'll just exclude them
        contacts = []
        for address in self.cleaned_data['to_addresses'].split(','):
            # First check if there is a group with this ID
            # TODO: Use a pretend email address instead of ID
            try:
                group = Group.objects.get(pk=100)
                contacts = contacts + group.contacts.all()
            except Group.DoesNotExist:
                try:
                    contact = Contact.objects.get(email=address)
                    contacts.append(contact)
                except Contact.DoesNotExist:
                    pass # TODO: Create an ad-hoc contact
        return contacts