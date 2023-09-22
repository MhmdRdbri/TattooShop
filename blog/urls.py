from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("blog/", views.article_list, name="articles_list"),
    path("<slug:slug>/", views.article_detail, name="articles_detail"),
    path("category/<slug:category_slug>/", views.article_list_by_category, name="articles_by_category"),
]
