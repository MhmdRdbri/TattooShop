from django.urls import path
from . import views

app_name = "pattern"
urlpatterns = [
    path("", views.pattern_list, name="pattern_list"),
    path("<slug:slug>/", views.pattern_detail, name="pattern_detail"),
]
