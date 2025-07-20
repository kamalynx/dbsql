from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.sitemaps.views import sitemap

from articles.sitemaps import ArticlesSitemap


sitemaps = {
    'articles': ArticlesSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap',
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    urlpatterns += debug_toolbar_urls()

urlpatterns += [path('', include('articles.urls'))]  # без этого "хака" debug toobar не хочет работать о_О
