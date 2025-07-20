import shutil
from pathlib import Path

from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django_resized import ResizedImageField
from slugify import slugify


def article_image_path(instance, filename):
    _, ext = filename.rsplit('.', 1)
    name = '.'.join([slugify(instance.title), ext])
    return f'articles/{instance.slug}/{name}'


def category_image_path(instance, filename):
    _, ext = filename.rsplit('.', 1)
    name = '.'.join([slugify(instance.title), ext])
    return f'categories/{instance.slug}/{name}'


class PublishedManager(models.Manager):

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('category').filter(is_published=True)


class Category(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.CharField('описание', max_length=512, blank=True)
    slug = models.SlugField('URI', max_length=80, unique=True)
    image = ResizedImageField('изображение', size=(320, 240), upload_to=category_image_path, blank=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('articles:category', kwargs={'slug': self.slug})


class Article(models.Model):
    title = models.CharField('заголовок', max_length=128)
    slug = models.SlugField('URI', max_length=80, unique=True)
    description = models.CharField('описание', max_length=512, blank=True)
    content = models.TextField('содержимое')
    image = ResizedImageField('изображение', upload_to=article_image_path, blank=True)
    is_published = models.BooleanField('опубликовано?', default=False)
    created_at = models.DateTimeField("дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("дата обновления", auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='категория', related_name='articles')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ('-created_at', '-updated_at')
        get_latest_by = ('-updated_at', '-created_at')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('articles:article', kwargs={'category': self.category.slug, 'slug': self.slug})

    def delete(self, **kwargs):
        if self.image:
            path = Path(self.image.path)

            self.image.delete()

            if path.parent.exists():
                shutil.rmtree(path.parent)

        super().delete(**kwargs)

