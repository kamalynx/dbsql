from django.contrib import admin

from articles import models, forms


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    form = forms.Article


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    form = forms.Category
