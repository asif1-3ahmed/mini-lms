# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourseListCreateView.as_view(), name="courses-list"),
    path("<int:pk>/", views.CourseDetailView.as_view(), name="courses-detail"),
]
