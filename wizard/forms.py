from django import forms

class AdminForm(forms.Form):
    email_address = forms.EmailField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)