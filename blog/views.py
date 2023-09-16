from django.shortcuts import render, get_object_or_404, redirect
from blog.models import *
from django.core.paginator import Paginator
from .forms import *
from django.views.generic.base import View, TemplateView


def article_list(request):
    articles = Article.objects.all()
    category = Category.objects.all()
    latest = Article.objects.order_by('-created_at')[:3]
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
    comments = articles.comments.all()
    category = Category.objects.all()
    latest = Article.objects.order_by('-created')[:3]
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.POST.get('parent_comment_id')
            parent_comment = None

            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, pk=parent_comment_id)
            new_comment = form.save(commit=False)
            new_comment.article = articles
            new_comment.parent_comment = parent_comment
            new_comment.save()
            form = CommentForm()  # Clear the form after submission

        else:
            form = CommentForm()

    context = {
        'articles': articles,
        'category': category,
        'latest': latest,
        'comments': comments,
        'form': form,
    }
    return render(request, "blog/article_details.html", context)
