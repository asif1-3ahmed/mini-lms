# Project's main urls.py (e.g., backend/urls.py)

from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    # 1. DJANGO ADMIN PATH
    path('admin/', admin.site.urls),

    # 2. APPLICATION API ROUTES
    path('api/auth/', include('accounts.urls')),
]
