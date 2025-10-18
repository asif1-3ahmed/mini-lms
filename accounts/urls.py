from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views  # or from your_app import views, depending on your structure


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),

    # Catch-all for React SPA
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
