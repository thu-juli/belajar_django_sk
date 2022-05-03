from django.shortcuts import render
from .forms import ContactForm, FromModelFrom


def index(request):
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contacts/index.html', context)


def forms(request):
    formModel = FromModelFrom()
    context = {
        'formModel': formModel
    }
    return render(request, 'contacts/forms.html', context)
