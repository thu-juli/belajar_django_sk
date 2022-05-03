from django.shortcuts import render, redirect
from .models import FromModel
from .forms import ContactForm, FromModelFrom


def home(request):
    context = {
        'success': 'your success submit form using forms django'
    }
    return render(request, 'contacts/home.html', context)


def index(request):
    name = request.POST['name']
    email = request.POST['email']
    body = request.POST['body']
    date_birth = request.POST['date_birth']

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            FromModel.objects.create(
                name=name,
                email=email,
                body=body,
                date_birth=date_birth,
            )
            return redirect('contacts:home')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contacts/index.html', context)


def forms(request):
    if request.method == 'POST':
        form = FromModelFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:home')
    else:
        form = FromModelFrom()

    context = {
        'form': form
    }
    return render(request, 'contacts/forms.html', context)
