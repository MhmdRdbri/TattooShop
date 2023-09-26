from django.shortcuts import render
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
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
    z_samples = Samples.objects.filter(author='ضیائی')[:6]
    k_samples = Samples.objects.filter(author='کارآموز')[:6]
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            form = MessageForm()
    else:
        form = MessageForm()

    context = {
        'articles': articles,
        'most_watched_patterns': most_watched_patterns,
        'courses': courses,
        'form': form,
        'z_samples': z_samples,
        'k_samples': k_samples,
    }

    return render(request, "home_app/index.html", context)
