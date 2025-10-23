from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, login_user, UserViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('', include(router.urls)),
]
