from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/auth/courses/", include("courses.urls")),  # add this
]
