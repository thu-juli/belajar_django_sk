from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy


# Create your views here.


class SignUpView(CreateView):
    template_name = 'registration/signup_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(
            username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return redirect('home')
