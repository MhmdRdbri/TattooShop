from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator


def course_list(request):
    courses = Course.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(courses, 6)
    object_list = paginator.get_page(page_number)

    context = {
        'courses': object_list,

    }
    return render(request, "blog/articles_list.html", context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
