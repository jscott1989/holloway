from django import forms
from django.forms import ModelForm
from models import EmailTemplate, SMTPAccount
from contacts.models import Contact, Group
from holloway.forms import ListField

class EmailTemplateForm(ModelForm):
    class Meta:
        model = EmailTemplate
        fields = ("subject", "html", "text", "required_fields")

class AccountForm(ModelForm):
    class Meta:
        model = SMTPAccount
        fields = ("email_address", "smtp_host", "smtp_port", "smtp_username", "smtp_password")

class EmailForm(forms.Form):
    to_addresses = forms.CharField(label="To")
    from_account = forms.ModelChoiceField(None, label="From")
    subject = forms.CharField(max_length=100)
    html = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.HiddenInput())
    required_fields = ListField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['from_account'].queryset = user.accounts

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