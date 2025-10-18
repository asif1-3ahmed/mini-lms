from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'  # Make sure this stays private
DEBUG = True
ALLOWED_HOSTS = [
    "mini-lms-bc6d.onrender.com",  # Add your Render domain here
    "localhost",
    "127.0.0.1",
]

# ------------------------------------------
# 🔹 INSTALLED_APPS
# ------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 👇 Add these for React
    "corsheaders",
    "rest_framework",
    
    # 👇 Your custom apps
    "accounts",
]
# ------------------------------------------

# ------------------------------------------
# 🔹 MIDDLEWARE
# ------------------------------------------
MIDDLEWARE = [
    # 👇 Must come at the top (before CommonMiddleware)
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# ------------------------------------------

# ------------------------------------------
# 🔹 STATIC FILES
# ------------------------------------------
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Serving React's static files
STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'build' / 'static',  # Path to React build static files
]

# ------------------------------------------

# ------------------------------------------
# 🔹 TEMPLATES
# ------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'frontend' / 'build'],  # Directory where React's index.html is located
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
# ------------------------------------------

# ------------------------------------------
# 🔹 WSGI APPLICATION
# ------------------------------------------
WSGI_APPLICATION = "backend.wsgi.application"
# ------------------------------------------

# ------------------------------------------
# 🔹 DATABASE
# ------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# ------------------------------------------

# ------------------------------------------
# 🔹 PASSWORD VALIDATORS
# ------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
# ------------------------------------------

# ------------------------------------------
# 🔹 INTERNATIONALIZATION
# ------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
# ------------------------------------------

# ------------------------------------------
# 🔹 CORS SETTINGS (for React frontend)
# ------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # For local development (React dev server)
    "http://127.0.0.1:5173",  # React dev server
    "https://your-frontend.vercel.app",  # Add your frontend domain here (e.g., Vercel)
]
CORS_ALLOW_CREDENTIALS = True
# ------------------------------------------

# ------------------------------------------
# 🔹 USER MODEL
# ------------------------------------------
AUTH_USER_MODEL = 'accounts.User'
# ------------------------------------------

# ------------------------------------------
# 🔹 STATIC URL
# ------------------------------------------
# Ensure there is only one STATIC_URL setting
STATIC_URL = '/static/'
# ------------------------------------------
