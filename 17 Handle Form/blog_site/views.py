from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'blog_site/index.html')


def contact(request):
    form = ContactForm()
    return render(request, 'blog_site/contact.html', {'form': form})
