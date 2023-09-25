from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import *


def sample_list(request):
    samples = Samples.objects.all()
    tags = Tags.objects.all()
    category_title = request.GET.get('category', None)
    if category_title:
        samples = Samples.objects.filter(category__title=category_title)
    else:
        samples = Samples.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(samples, 9)
    object_list = paginator.get_page(page_number)

    categories = SamplesCategory.objects.all()

    context = {
        'samples': object_list,
        'categories': categories,
        'selected_category': category_title,
        'tags': tags,
    }
    return render(request, "samples/samples_list.html", context)


def sample_detail(request, slug):
    sample = get_object_or_404(Samples, slug=slug)

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
            new_comment.sample = sample  # Set the pattern relationship
            new_comment.parent_comment = parent_comment
            new_comment.save()

            form = CommentForm()  # Clear the form after submission

    context = {
        'sample': sample,
        'form': form,
    }
    return render(request, "samples/samples_detail.html", context)
