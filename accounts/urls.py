# Project's main urls.py (e.g., backend/urls.py)

from django.contrib import admin
from django.urls import path, re_path, include
from accounts.views import IndexView # <--- Make sure this is imported

urlpatterns = [
    # 1. DJANGO ADMIN PATH
    path('admin/', admin.site.urls),

    # 2. APPLICATION API ROUTES
    path('api/auth/', include('accounts.urls')),

    # 3. FRONTEND SPA ROUTE (MUST BE LAST)
    re_path(r'^(?!admin/|api/|assets/|static/).*$', 
            IndexView.as_view(), 
            name='react_app_root'),
]
