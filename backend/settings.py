from pathlib import Path
import os

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['mini-lms-crh4.onrender.com', 'localhost', '127.0.0.1']

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "accounts",  # Your custom app
]

# Static files settings
STATIC_URL = '/static/'  # URL for accessing static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where to collect static files in production

# Directories for collecting static files during development
STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'dist' / 'assets',  # Path to React build folder's assets
]

# Middleware to serve static files efficiently
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Whitenoise should be included here
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# URL configuration (points to accounts.urls for routing)
ROOT_URLCONF = 'accounts.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend' / 'dist'],  # Ensure index.html is here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CORS settings for cross-origin requests
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend.vercel.app",
    "http://localhost:5173",  # Local development server
]

CORS_ALLOW_CREDENTIALS = True

# Custom user model for accounts app
AUTH_USER_MODEL = 'accounts.User'

# Don't forget to run collectstatic after changes
