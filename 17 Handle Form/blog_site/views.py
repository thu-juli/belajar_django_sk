from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
from django.contrib import messages


def index(request):
    return render(request, 'blog_site/index.html')


def contact(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Berhasil Kirim Email')
            return HttpResponseRedirect(reverse('contact'))

    return render(request, 'blog_site/contact.html', {'form': form})
