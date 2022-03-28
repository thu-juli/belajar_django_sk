from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    desc = forms.CharField(widget=forms.Textarea())
