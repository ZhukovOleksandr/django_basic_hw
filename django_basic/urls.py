from django.urls import path, re_path
from django_basic.views import *


urlpatterns = [
    path('articles/', articles, name='articles'),
    path('articles/archive', archive, name='archive'),
    path('users/', user, name='users'),
    path('users/<int:user_number>/', user, name='users'),
    path('users/<int:article_number>/', article, name='article'),
    path('article/<int:article_number>/', article, name='article-number'),
    path('article/<int:article_number>/archive', archive, name='article-archive'),
    path('article/<int:article_number>/<slug:slug_text>', article, name='article-slug'),
    re_path(r'^number/(?P<numb>[0-9]{10}/$)', number_validator, name='numb_valid'),
    re_path(r'^numbers/(?P<value>[0-9a-z]{4}-[0-9a-z]{6}/$)', some_view, name='some_view'),
]