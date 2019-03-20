from django.urls import path
from . import views

urlpatterns = [
    #     path('',views.index,name='index'),
    #   path('post/list/', views.ArticleList.as_view(),name='article_list'),
    #     path('post/detail/<pk>/',views.ArticleDetail.as_view(),name='article_detail'),
    path('post/delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article_list/', views.ArticleList.as_view(), name='article_list'),
    path('post/update/<pk>/', views.ArticleUpdate.as_view(), name='post_update'),

]
