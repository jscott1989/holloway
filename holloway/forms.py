from django import forms

class ListField(forms.CharField):
    """ Field which activates the associated list logic if listfield.coffee is included. """
    def __init__(self, *args, **kwargs):
        kwargs['initial'] = kwargs.get('initial', "[]")
        kwargs['widget'] = forms.Textarea(attrs={"class": "type_listfield"})
        super(ListField, self).__init__(*args, **kwargs)