from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key secret in production!
# Use environment variable, with a fallback for local development.
SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "mini-lms-crh4.onrender.com",
    "localhost",
    "127.0.0.1",
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise must be listed immediately after SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware", 
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # you can add template directories here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # required by admin
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Root URL Configuration
ROOT_URLCONF = "backend.urls" # Confirmed to be your main router
WSGI_APPLICATION = "backend.wsgi.application"

# --- Database Configuration (Critical Production Fix) ---
# Uses dj-database-url to handle both local SQLite (default) and 
# PostgreSQL (via DATABASE_URL environment variable on Render).
DATABASES = {
    "default": dj_database_url.config(
        # Fallback to local SQLite if DATABASE_URL is not set (e.g., local dev)
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# --- Static files (React + Django) ---
STATIC_URL = "/static/"
# Where collected files go after python manage.py collectstatic
STATIC_ROOT = BASE_DIR / "staticfiles"
# Where collectstatic looks for static files (the Vite/React build output)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# --- CORS ---
CORS_ALLOWED_ORIGINS = [
    "https://mini-lms-1.onrender.com",  # your frontend
    "http://localhost:5173",            # local dev
]

CORS_ALLOW_CREDENTIALS = True

# User Model and Default Fields
AUTH_USER_MODEL = "accounts.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
