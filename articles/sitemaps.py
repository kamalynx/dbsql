from django.contrib.sitemaps import Sitemap

from articles.models import Article


class ArticlesSitemap(Sitemap):
    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
