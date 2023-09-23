from django.urls import path
from . import views

app_name = "course"
urlpatterns = [
    path("course/", views.course_list, name="course_list"),
    # path("<slug:slug>/", views.article_detail, name="articles_detail"),
]