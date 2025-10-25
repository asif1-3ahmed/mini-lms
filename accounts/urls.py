from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, login_user, logout_user, profile
from courses.views import CourseViewSet  # ✅ import from courses

# Register Course API endpoints with DRF's router
router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', profile, name='user_profile'),
    path('', include(router.urls)), 
    path('api/', include('courses.urls')) # Courses API will be available here
]
