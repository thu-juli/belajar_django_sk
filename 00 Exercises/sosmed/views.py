from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from .models import Profile
from .forms import ProfileForm


class FormView(View):
    template_name = 'sosmed/form.html'
    form = ProfileForm()
    mode = None
    context = {}

    def get(self, request, **kwargs):
        if self.mode == 'update':
            dataForm = Profile.objects.get(id=kwargs['id'])
            self.form = ProfileForm(instance=dataForm)
            self.context['form'] = self.form

        else:
            self.context['form'] = self.form

        return render(request, self.template_name, self.context)

    def post(self, request, **kwargs):
        if self.mode == 'update':
            dataForm = Profile.objects.get(id=kwargs['id'])
            self.form = ProfileForm(request.POST, instance=dataForm)
            if self.form.is_valid():
                self.form.save()
                return redirect('sosmed:list-view')
        else:
            self.form = ProfileForm(request.POST)
            if self.form.is_valid():
                self.form.save()
                return redirect('sosmed:list-view')

        return render(request, self.template_name, self.context)


class ListView(TemplateView):
    template_name = 'sosmed/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profiles'] = Profile.objects.all()
        return context


class DetailView(TemplateView):
    template_name = 'sosmed/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.get(id=kwargs['id'])
        return context


class DeleteView(RedirectView):
    pattern_name = 'sosmed:list-view'

    def get_redirect_url(self, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        profile.delete()
        return super().get_redirect_url()
