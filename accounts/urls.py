from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    re_path(r'^(?!assets/|static/|admin/|api/).*$', 
            TemplateView.as_view(template_name='index.html'), 
            name='react_app'),
]
