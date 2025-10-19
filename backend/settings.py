from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'  # make sure this stays private
DEBUG = True
ALLOWED_HOSTS = [
    'mini-lms-crh4.onrender.com',
    'localhost', 
    '127.0.0.1',
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

    # 👇 Add these 2
    "corsheaders",
    "rest_framework",
    

    # 👇 Add your custom apps here
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
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
CORS_ALLOW_ALL_ORIGINS = True
# ------------------------------------------

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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
# 🔹 PASSWORD VALIDATORS
# ------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ------------------------------------------
# 🔹 INTERNATIONALIZATION
# ------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ------------------------------------------
# 🔹 STATIC FILES
# ------------------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'frontend/dist',  # Adjust this path if needed
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------
# 🔹 CORS SETTINGS (for React frontend)
# ------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_CREDENTIALS = True
AUTH_USER_MODEL = 'accounts.User'


CORS_ALLOWED_ORIGINS = [
    "https://your-frontend.vercel.app",
    "http://localhost:5173",  # keep for local dev
]
STATIC_URL = '/static/'

