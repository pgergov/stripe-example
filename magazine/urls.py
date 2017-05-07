from django.conf.urls import url, include

from .views import ArticleList, MagazineList


article_patterns = [
    url(
        regex='^$',
        view=ArticleList.as_view(),
        name='list'
    )
]


urlpatterns = [
    url(
        regex='^$',
        view=MagazineList.as_view(),
        name='list'
    ),
    url(
        regex='^(?P<magazine_id>[0-9]+)/article/',
        view=include(
            arg=article_patterns,
            namespace='article'
        )
    )
]
