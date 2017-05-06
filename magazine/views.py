from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .tasks import charge
from .models import Article, Magazine


class MagazineList(LoginRequiredMixin, ListView):
    model = Magazine


class ArticleList(LoginRequiredMixin, ListView):
    model = Article

    def get_queryset(self):
        return self.model.objects\
                         .filter(magazine_id=self.kwargs['magazine_id'])


class BuyArticleView(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse('magazine:article:list', kwargs=self.kwargs)

    def post(self, request, *args, **kwargs):
        charge.delay()

        return redirect(self.get_success_url())
