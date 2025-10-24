from pathlib import Path
import os
import dj_database_url

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-&by_duh@h9@=ao+_@4%m3=17nmvj4ptmpa7dih+*rkr%pj-39-"
)
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = [
    "mini-lms-crh4.onrender.com",  # backend render domain
    "localhost",
    "127.0.0.1",
]

# --------------------------------------------------------------------
# Installed apps
# --------------------------------------------------------------------
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "corsheaders",
    "rest_framework",

    # Local apps
    "accounts",
]

# --------------------------------------------------------------------
# Middleware
# --------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # must be before CommonMiddleware
    "django.contrib.sessions.middleware.SessionMiddleware",  # must be before CommonMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

# --------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Add template paths if needed
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# --------------------------------------------------------------------
# Database
# --------------------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# --------------------------------------------------------------------
# Password validation
# --------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------------------------
# Internationalization
# --------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------
# Static files
# --------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------------------------
# CORS configuration
# --------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "https://mini-lms-1.onrender.com",  # frontend render domain
    "http://localhost:5173",            # local dev
]
CORS_ALLOW_CREDENTIALS = True

# --------------------------------------------------------------------
# Session & CSRF settings
# --------------------------------------------------------------------
SESSION_COOKIE_SECURE = False  # True in production HTTPS
CSRF_COOKIE_SECURE = False     # True in production HTTPS
SESSION_COOKIE_SAMESITE = 'Lax'  # 'None' if cross-site with HTTPS
CSRF_COOKIE_SAMESITE = 'Lax'

# --------------------------------------------------------------------
# Authentication
# --------------------------------------------------------------------
AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
