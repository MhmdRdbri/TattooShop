from django.shortcuts import render, get_object_or_404, redirect
from blog.models import *
from django.core.paginator import Paginator
# from .forms import *
from django.views.generic.base import View, TemplateView


def article_list(request):
    articles = Article.objects.all()
    category = Category.objects.all()
    latest = Article.objects.order_by('-created')[:3]
    most_watched_blogs = Article.objects.order_by('-view_count')[:6]
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    context = {
        'articles': object_list,
        'category': category,
        'latest': latest,
        'most_watched_blogs': most_watched_blogs,
    }
    return render(request, "blog/articles_list.html", context)