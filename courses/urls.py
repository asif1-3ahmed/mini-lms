# courses/urls.py
from django.urls import path
from .views import CourseListCreateView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course_list_create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
