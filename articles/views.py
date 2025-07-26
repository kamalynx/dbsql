from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.http import last_modified
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Count

from articles import models


def get_article_modified_date(request, **kwargs):
    entry = models.Article.objects.values('updated_at').get(
        slug=kwargs['slug']
    )
    return entry['updated_at']


class Articles(ListView):
    model = models.Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'PAGINATE_BY', 2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canonical'] = self.request.build_absolute_uri(reverse_lazy('articles:articles'))

        page_number = context['page_obj'].number
        if page_number == 1:
            context['title'] = self.request.site.name
        else:
            context['title'] = f'Страница {page_number} — {self.request.site.name}'

        return context


# ~ @method_decorator(last_modified(get_article_modified_date), name='dispatch')
class Article(DetailView):
    model = models.Article
    template_name = 'articles/single.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canonical'] = self.request.build_absolute_uri(self.get_object().get_absolute_url())
        return context


class Category(DetailView):
    model = models.Category
    template_name = 'articles/category.html'
    context_object_name = 'category'

    def get_queryset(self):
        return super().get_queryset().annotate(
            articles_count=Count('articles')
        ).filter(articles_count__gt=0)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.object.articles.all()
        return context
