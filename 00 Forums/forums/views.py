from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Forum
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

"""
Note!!!
- Adding method Ownership
"""


@method_decorator(login_required, name='dispatch')
class ForumDelete(DeleteView):
    model = Forum
    success_url = reverse_lazy('forums:list')


"""
Note!!!
- Adding method Ownership
- Custom template_name ForumUpdate
"""


@method_decorator(login_required, name='dispatch')
class ForumUpdate(UpdateView):
    model = Forum
    fields = [
        'title',
        'content'
    ]


class ForumList(ListView):
    model = Forum


class ForumDetail(DetailView):
    model = Forum


@method_decorator(login_required, name='dispatch')
class ForumCreate(CreateView):
    model = Forum
    fields = [
        'title',
        'content'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
