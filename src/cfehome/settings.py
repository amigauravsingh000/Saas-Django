"""
Django settings for cfehome project (Render Ready & Local Dev Compatible)
"""

import os
from pathlib import Path
import dj_database_url  # pip install dj-database-url
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Load environment variables
# SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-default-secret-key")
SECRET_KEY = config("DJANGO_SECRET_KEY", default = "unsafe-default-secret-key")

# ✅ Default DEBUG=True for local dev unless explicitly set to False
# DEBUG = os.environ.get("DEBUG", "False") == "True"
DEBUG = config("DJANGO_DEBUG", cast=bool)
print("DEBUG", DEBUG, type(DEBUG))
# ✅ Allowed Hosts
ALLOWED_HOSTS = [".onrender.com"]
if DEBUG:
    ALLOWED_HOSTS += ["127.0.0.1", "localhost"]

# ✅ Database configuration
# DATABASE_URL = os.environ.get("DATABASE_URL")
CONN_MAX_AGE = config("CONN_MAX_AGE", cast=int, default = 30)
DATABASE_URL = config("DATABASE_URL", cast=str)

if DATABASE_URL is not None:
    # ✅ Render PostgreSQL with SSL
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_health_checks=True,
            conn_max_age=CONN_MAX_AGE,
            # ssl_require=True
        )
    }
else:
    # ✅ Local SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ✅ CSRF Trusted Origins (only add if value exists)
render_host = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_host:
    CSRF_TRUSTED_ORIGINS = [f"https://{render_host}"]
else:
    CSRF_TRUSTED_ORIGINS = []

# ✅ Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ✅ your apps
    'visits',
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Static files for production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cfehome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ✅ Custom templates folder
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

WSGI_APPLICATION = 'cfehome.wsgi.application'

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static files
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
