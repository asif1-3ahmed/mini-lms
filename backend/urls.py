from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),  # Include accounts app URLs here
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
