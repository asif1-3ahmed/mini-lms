from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, register_user, login_user, logout_user, profile

# DRF router for courses
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    # Auth endpoints
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),       # token-based login
    path('logout/', logout_user, name='logout_user'),    # optional, can delete token
    path('profile/', profile, name='user_profile'),

    # Include router-generated routes for courses
    path('', include(router.urls)),
]
