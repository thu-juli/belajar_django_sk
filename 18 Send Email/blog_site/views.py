from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from . import forms
from django.contrib import messages


def index(request):
    return render(request, 'blog_site/index.html')


def contact(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # send mail
            send_mail('Dari Mywebsite',
                      request.POST['desc'],
                      request.POST['email'],
                      [
                          'thujuli@test.com',
                      ])

            # message sucess
            messages.success(request, 'Berhasil Kirim Pesan')
            return HttpResponseRedirect(reverse('contact'))

    return render(request, 'blog_site/contact.html', {'form': form})
