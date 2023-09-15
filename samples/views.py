from django.shortcuts import render
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
