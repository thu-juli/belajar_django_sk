from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

# Create your views here.


class SignUpView(CreateView):
    template_name = 'registration/signup_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
