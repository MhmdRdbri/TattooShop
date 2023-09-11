from django.shortcuts import render, get_object_or_404, redirect
from blog.models import *
from django.core.paginator import Paginator
# from .forms import *
from django.views.generic.base import View, TemplateView


def article_list(request):
    articles = Article.objects.all()
    category = Category.objects.all()
    latest = Article.objects.order_by('-created')[:3]
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    context = {
        'articles': object_list,
        'category': category,
        'latest': latest,
    }
    return render(request, "blog/articles_list.html", context)


def article_detail(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    category = Category.objects.all()
    latest = Article.objects.order_by('-created')[:3]
    # if request.method == 'POST':
    #     parent_id = request.POST.get('parent_id')
    #     body = request.POST.get('body')
    #     Comment.objects.create(body=body, article=articles, user=request.user, parent_id=parent_id)

    context = {
        'articles': articles,
    }
    return render(request, "blog/article_details.html", context)
