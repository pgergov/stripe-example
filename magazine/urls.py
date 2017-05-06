from django.conf.urls import url

from .views import ArticleList


urlpatterns = [
    url(
        regex='^$',
        view=ArticleList.as_view(),
        name='list'
    )
]
