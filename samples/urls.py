from django.urls import path
from . import views

app_name = "samples"
urlpatterns = [
    path("", views.sample_list, name="samples_list"),
    path("<slug:slug>/", views.sample_detail, name="samples_detail"),
]
