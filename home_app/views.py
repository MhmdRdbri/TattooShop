from django.shortcuts import render
from .forms import *
from pattern.models import *

# most_watched_blogs = Pattern.objects.order_by('-view_count')[:6]