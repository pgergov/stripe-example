from django.conf import settings
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, Magazine


class MagazineList(LoginRequiredMixin, ListView):
    model = Magazine

    def get_context_data(self):
        context = super().get_context_data()
        context['stripe_pk'] = settings.STRIPE_PUBLIC_KEY

        return context


class ArticleList(LoginRequiredMixin, ListView):
    model = Article

    def get_queryset(self):
        return self.model.objects\
                         .filter(magazine_id=self.kwargs['magazine_id'])
