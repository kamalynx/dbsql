from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.http import last_modified

from articles import models


def get_article_modified_date(request, **kwargs):
    entry = models.Article.objects.values('updated_at').get(
        slug=kwargs['slug']
    )
    return entry['updated_at']


class Articles(ListView):
    model = models.Article
    queryset = models.Article.published.all()
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return models.Article.published.all()
        return super().get_queryset()


@method_decorator(last_modified(get_article_modified_date), name='dispatch')
class Article(DetailView):
    model = models.Article
    queryset = models.Article.published.all()
    template_name = 'articles/single.html'
    context_object_name = 'article'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return models.Article.published
        return super().get_queryset()


class Category(DetailView):
    model = models.Category
    # ~ queryset = models.Category
    template_name = 'articles/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.object.articles.filter(is_published=True)
        return context

