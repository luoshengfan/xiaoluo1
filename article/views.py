from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article


# Create your views here.
def index(request):
    return render(request, 'index.html')




def article_delete(request, id):
    Articles = Article.objects.get(id=id)
    Articles.delete()


#     return redirect('post_list')


class ArticleDetail(DetailView):
    model = Article
    template_name = 'post_detail.html'



class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'post_update.html'
    
class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'


