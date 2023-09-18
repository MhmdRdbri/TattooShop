from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator


def pattern_list(request):
    patterns = Pattern.objects.all()
    category_title = request.GET.get('category', None)
    if category_title:
        patterns = Pattern.objects.filter(category__title=category_title)
    else:
        patterns = Pattern.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(patterns, 9)
    object_list = paginator.get_page(page_number)

    categories = PatternCategory.objects.all()

    context = {
        'patterns': object_list,
        'categories': categories,
        'selected_category': category_title,
    }
    return render(request, "blog/articles_list.html", context)


def pattern_detail(request, slug):
    patterns = get_object_or_404(Pattern, slug=slug)

    client_ip = get_client_ip(request)
    existing_log_entry = PatternPostViewLog.objects.filter(
        pattern_post=patterns,
        ip_address=client_ip
    ).first()

    if not existing_log_entry:
        PatternPostViewLog.objects.create(
            blog_post=patterns,
            ip_address=client_ip
        )
        patterns.view_count += 1
        patterns.save()

    return render(request, "blog/articles_list.html", {'patterns': patterns})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
