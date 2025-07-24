from django.contrib import admin

from articles import models, forms


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    form = forms.Article

    class Media:
        js = ('tinymce/tinymce.min.js', 'admin.js')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    form = forms.Category
