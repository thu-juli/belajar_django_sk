from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, RedirectView, View
from .models import Article
from .forms import FormArticle


class BlogListView(TemplateView):
    template_name = 'blog/list.html'

    def get_context_data(self, *args, **kwargs):
        queryset = Article.objects.all()
        extra_context = {
            'page_title': 'List-View',
            'queryset': queryset
        }
        return extra_context


class DeleteListView(RedirectView):
    pattern_name = 'blog:list-view'

    def get_redirect_url(self, *args, **kwargs):
        deleteId = kwargs['deleteId']
        Article.objects.filter(id=deleteId).delete()
        return super().get_redirect_url()


class FromListView(View):
    template_name = 'blog/form.html'
    form = FormArticle
    mode = None
    context = {}

    def get(self, request, *args, **kwargs):
        if self.mode == 'update':
            instance = Article.objects.get(slug=kwargs['slug'])
            self.form = FormArticle(instance=instance)

        self.context = {
            'form': self.form
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if self.mode == 'update':
            instance = Article.objects.get(slug=kwargs['slug'])
            form = self.form(request.POST, instance=instance)
        else:
            form = self.form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blog:list-view')

        return render(request, self.template_name, self.context)
