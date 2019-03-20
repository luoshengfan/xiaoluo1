from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  .models import  Article
# Create your views here.

class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
