from django.contrib import admin

from users.models import Author, Buyer


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'age', 'interests')


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'came_from', )
