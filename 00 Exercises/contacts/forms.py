from django import forms
from django.forms import ModelForm
from .models import FromModel


class ContactForm(forms.Form):
    SUBJECT_CHOICES = [
        ('1', 'web dev'),
        ('2', 'backend'),
        ('3', 'frontend'),
    ]

    name = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField(
        widget=forms.Textarea()
    )
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    date_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )


class FromModelFrom(ModelForm):
    class Meta:
        model = FromModel
        fields = '__all__'
        widgets = {
            'subject': forms.CheckboxSelectMultiple(),
            'date_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }
