from django.contrib import admin
from django.urls import path, re_path, include
from accounts.views import IndexView # <--- Make sure you import IndexView

urlpatterns = [
    # 1. DJANGO ADMIN
    path('admin/', admin.site.urls),

    # 2. APPLICATION API ROUTES
    # All API calls will start with /api/auth/
    path('api/auth/', include('accounts.urls')),

    # 🛑 CRITICAL FIX: Removed duplicate login/register path('',...) from accounts.urls

    # 3. FRONTEND SPA ROUTE (MUST BE LAST)
    # This catches the root path (''), any single route ('/dashboard'), 
    # and any deep route ('/course/123').
    re_path(r'^$', IndexView.as_view()), # Catches the root: /
    re_path(r'^(?:.*)/?$', IndexView.as_view(), name='react_app'), # Catches all sub-paths
]
