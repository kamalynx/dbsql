from django.urls import path

from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.Articles.as_view(), name='articles'),
    path('page/<page>/', views.Articles.as_view(), name='pages'),
    path('<slug:category>/<slug:slug>/', views.Article.as_view(), name='article'),
    path('<slug:slug>/', views.Category.as_view(), name='category'),
]
