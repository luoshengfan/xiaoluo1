from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Article


# Create your views here.
def index(request):
    return render(request, 'index.html')


class ArticleList(ListView):
    model = Article
    template_name = 'post_list.html'


def article_delete(request, id):
    Articles =Article.objects.get(id=id)
    Articles.delete()
    return redirect('post_list')


class  ArticleDetail(DetailView):
    model = Article
    template_name = 'post_detail.html'

