from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'update_article.html', {'form': form})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})