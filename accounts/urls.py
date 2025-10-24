from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, register_user, login_user, logout_user, profile

# Register Course API endpoints with DRF's router
router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('api/register/', register_user, name='register_user'),
    path('api/login/', login_user, name='login_user'),
    path('api/logout/', logout_user, name='logout_user'),
    path('api/profile/', profile, name='user_profile'),
    path('api/', include(router.urls)),  # Courses API will be available here
]
