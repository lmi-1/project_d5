from django.urls import path
from .views import (
    PostsList, PostDetail, PostsSearch,
    NewsCreate, NewsUpdate, NewsDelete,
    ArticleCreate, ArticleUpdate, ArticleDelete
)

urlpatterns = [
    path('news/', PostsList.as_view(), name='posts_list'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/search/', PostsSearch.as_view(), name='posts_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]
