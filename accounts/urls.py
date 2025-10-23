# accounts/urls.py
from django.urls import path
from . import views  # import your views here

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
]
