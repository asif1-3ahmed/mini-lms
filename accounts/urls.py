from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views # or from your_app import views (if this is the project-level urls.py)


urlpatterns = [
    # 1. DJANGO ADMIN
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')), 
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    re_path(r'^(?!static/)(?:.*)/?$', TemplateView.as_view(template_name='index.html')),
]
