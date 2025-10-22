# Project's main urls.py (e.g., backend/urls.py)

from django.contrib import admin
from django.urls import path, re_path, include
# Assuming your IndexView is in accounts/views.py
from accounts.views import IndexView 

urlpatterns = [
    # 1. DJANGO ADMIN PATH
    path('admin/', admin.site.urls),

    # 2. APPLICATION API ROUTES
    # All API calls (register, login, etc.) will start with /api/auth/
    path('api/auth/', include('accounts.urls')),

    # 3. FRONTEND SPA ROUTE (MUST BE LAST)
    # This regex is simple and robust: it catches everything *except* # the paths defined above and passes them to the IndexView.

    # It catches the root ('/') and all other React routes (e.g., /dashboard, /course/1)
    re_path(r'^(?!admin/|api/|assets/|static/).*$', 
            IndexView.as_view(), 
            name='react_app_root'),
]
