from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from .forms import *


def pattern_list(request):
    patterns = Pattern.objects.all()
    tags = Tags.objects.all()
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
        'tags': tags,
    }
    return render(request, "pattern/pattern_list.html", context)


def pattern_detail(request, slug):
    pattern = get_object_or_404(Pattern, slug=slug)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.POST.get('parent_comment_id')
            parent_comment = None

            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, pk=parent_comment_id)

            # Create the comment, set the pattern field, and save it
            new_comment = form.save(commit=False)
            new_comment.pattern = pattern  # Set the pattern relationship
            new_comment.parent_comment = parent_comment
            new_comment.save()

            form = CommentForm()  # Clear the form after submission

    client_ip = get_client_ip(request)
    existing_log_entry = PatternPostViewLog.objects.filter(
        pattern_post=pattern,
        ip_address=client_ip
    ).first()

    if not existing_log_entry:
        PatternPostViewLog.objects.create(
            pattern_post=pattern,
            ip_address=client_ip
        )
        pattern.view_count += 1
        pattern.save()

    return render(request, "pattern/pattern_detail.html", {'pattern': pattern, 'form': form})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
