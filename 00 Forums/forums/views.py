from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Forum
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class OwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(obj)
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ForumDelete(OwnerMixin, DeleteView):
    model = Forum
    success_url = reverse_lazy('forums:list')


@method_decorator(login_required, name='dispatch')
class ForumUpdate(OwnerMixin, UpdateView):
    model = Forum
    template_name = 'forums/forum-edit_form.html'
    fields = [
        'title',
        'content'
    ]


class ForumList(ListView):
    model = Forum
    ordering = ['-created']


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
