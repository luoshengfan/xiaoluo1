from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    article = Article.objects.all()
    return render(request, 'index.html', {'article': article})


class ArticleCreate(CreateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_cerate.html'
    success_url = reverse_lazy('index')


def article_delete(request, id):
    Articles = Article.objects.get(id=id)
    Articles.delete()
    return redirect('/')


class ArticleDetail(DetailView):
    model = Article
    template_name = 'post_detail.html'


class ArticleUpdate(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'post_update.html'
    success_url = reverse_lazy('index')


class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
