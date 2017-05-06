from django.views.generic.list import ListView

from .models import Article


class ArticleList(ListView):
    model = Article
    fields = ('title', 'author')
