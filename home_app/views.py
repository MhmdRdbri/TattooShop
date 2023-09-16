from django.shortcuts import render
from .forms import *
from pattern.models import *
from samples.models import *
from blog.models import *
from course.models import *


def home(request):
    articles = Article.objects.order_by('-created_at')[:6]
    most_watched_patterns = Pattern.objects.order_by('-view_count')[:6]
    courses = Course.objects.all()[:6]
    form = MessageForm()
