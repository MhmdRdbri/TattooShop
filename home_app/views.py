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
    z_samples = Samples.objects.filter(author='Z')[:6]
    k_samples = Samples.objects.filter(author='K')[:6]
    if request.method == 'POST':
        form = MessageForm(data=request.POST)

        if form.is_valid():
            # Extract the email field value from the form
            email = form.cleaned_data['Email']

            # Create an EmailValidator instance
            email_validator = EmailValidator()

            try:
                # Validate the email using the EmailValidator
                email_validator(email)

                form.save()

            except ValidationError:
                # If validation fails, handle the error (e.g., show an error message)
                # You can customize this part to handle the validation error as you prefer
                # For example, you could add an error message to the form
                form.add_error('Email', 'Invalid email address!')
        else:
            # Form is not valid, you can handle this as needed
            # For example, you could display an error message to the user
            form.add_error('Name', 'Invalid form!')

    context = {
        'articles': articles,
        'most_watched_patterns': most_watched_patterns,
        'courses': courses,
        'form': form,
        'z_samples': z_samples,
        'k_samples': k_samples,
    }

    return render(request, "home_app/index.html", context)
