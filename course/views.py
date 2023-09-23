from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from blog.models import *
from .forms import *


def course_list(request):
    courses = Course.objects.all()
    tags = Tags.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(courses, 6)
    object_list = paginator.get_page(page_number)

    context = {
        'courses': object_list,
        'tags': tags,
    }
    return render(request, "course/course_list.html", context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    comments = course.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.POST.get('parent_comment_id')
            parent_comment = None

            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, pk=parent_comment_id)
            new_comment = form.save(commit=False)
            new_comment.course = course
            new_comment.parent_comment = parent_comment
            new_comment.save()
            form = CommentForm()  # Clear the form after submission
        else:
            form = CommentForm()

    context = {
        'courses': course,
        'comments': comments,
        'form': form,
    }
    return render(request, "course/course_detail.html", context)
