# accounts/urls.py
from django.urls import path, include
from .views import register_user, login_user, logout_user, profile
from rest_framework.routers import DefaultRouter
from courses.views import CourseListCreateView, CourseDetailView

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', profile, name='user_profile'),

    # Include the course-related endpoints here
    path('courses/', CourseListCreateView.as_view(), name='course_list_create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]

