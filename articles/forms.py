from django import forms

from articles import models


class SimpleForm(forms.ModelForm):

    class Meta:
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
        fields = '__all__'


class Category(SimpleForm):

    class Meta(SimpleForm.Meta):
        model = models.Category


class Article(SimpleForm):

    class Meta(SimpleForm.Meta):
        model = models.Article
