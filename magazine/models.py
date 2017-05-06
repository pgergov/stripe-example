from django.db import models

from users.models import Author


class Magazine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    magazine = models.ForeignKey(Magazine)
    author = models.ForeignKey(Author)

    def __str__(self):
        return "Article {} written by {}".format(self.title, self.author)
