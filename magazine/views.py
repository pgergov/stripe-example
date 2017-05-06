from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, Magazine


class MagazineList(LoginRequiredMixin, ListView):
    model = Magazine
    fields = ('name', )


class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    fields = ('title', 'author')

    def get_queryset(self):
        return self.model.objects.filter(magazine_id=self.kwargs['magazine_id'])
