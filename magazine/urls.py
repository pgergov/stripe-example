from django.conf.urls import url

from .views import ArticleList, MagazineList


urlpatterns = [
    url(
        regex='^$',
        view=MagazineList.as_view(),
        name='magazine-list'
    ),
    url(
        regex='^(?P<magazine_id>[0-9]+)/article$',
        view=ArticleList.as_view(),
        name='article-list'
    )
]
