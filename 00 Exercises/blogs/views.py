from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'page_title': 'CBV'
    }
    ordering = ['title']
    paginate_by = 2

    # def get_queryset(self, *args, **kwargs):
    #     print(kwargs)
    #     # self.queryset = Article.objects.filter()
    #     return super().get_queryset()

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)
