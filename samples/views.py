from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *


def sample_list(request):
    samples = Samples.objects.all()
    category_title = request.GET.get('category', None)
    if category_title:
        patterns = samples.objects.filter(category__title=category_title)
    else:
        patterns = samples.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(patterns, 9)
    object_list = paginator.get_page(page_number)

    categories = SamplesCategory.objects.all()

    context = {
        'samples': object_list,
        'categories': categories,
        'selected_category': category_title,
    }
    return render(request, "blog/articles_list.html", context)


def sample_detail(request, slug):
    samples = get_object_or_404(Samples, slug=slug)

    context = {
        'samples': samples,
    }
    return render(request, "blog/articles_list.html", context)

