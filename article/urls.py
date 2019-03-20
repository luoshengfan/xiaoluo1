from django.urls import path
from . import views

urlpatterns = [
    path('article_list/',views.ArticleList.as_view(),name='article_list')
]
