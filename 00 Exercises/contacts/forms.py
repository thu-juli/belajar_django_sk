from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm
from .models import FromModel


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit('submit', 'Submit'))

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

    def clean_name(self):
        data = self.cleaned_data['name']
        if data == 'Julianta':
            raise forms.ValidationError('Julianta itu nama gue')

        return data


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.add_input(Submit('submit', 'Submit'))
