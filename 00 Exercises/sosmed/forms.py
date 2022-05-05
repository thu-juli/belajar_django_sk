from django.forms import ModelForm
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))
