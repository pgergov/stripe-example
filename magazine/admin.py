from django.contrib import admin

from magazine.models import Magazine, Article


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'magazine', 'author')
