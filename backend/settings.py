from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['mini-lms-crh4.onrender.com', 'localhost', '127.0.0.1']

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
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Ensure Whitenoise is included
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATIC_URL = '/static/'

# Path to the frontend's build directory (React build)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'dist', 'assets'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
ROOT_URLCONF = 'accounts.urls'

# Template settings (adjust if needed)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'dist')],
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

CORS_ALLOWED_ORIGINS = [
    "https://your-frontend.vercel.app",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True
AUTH_USER_MODEL = 'accounts.User'

# Don't forget to run collectstatic after changes
