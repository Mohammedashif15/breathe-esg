import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# SECURITY
# ========================
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-breathe-esg-secret-key"
)

DEBUG = os.environ.get("DEBUG", "False") == "True"


# ========================
# ALLOWED HOSTS
# ========================
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
    ".railway.app",
    ".vercel.app",
]


# ========================
# INSTALLED APPS
# ========================
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ingestion',
    'emissions',
    'reviews',
]


# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


# ========================
# TEMPLATES
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'config.wsgi.application'


# ========================
# DATABASE (SQLite)
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ========================
# PASSWORD VALIDATION
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


# ========================
# INTERNATIONALIZATION
# ========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# ========================
# STATIC + MEDIA
# ========================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ========================
# DEFAULT PK
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ========================
# CORS + CSRF (IMPORTANT)
# ========================

# Replace with your actual Vercel URL
# ========================
# CORS + CSRF (IMPORTANT)
# ========================

CORS_ALLOWED_ORIGINS = [
    "https://breathe-esg-r57s.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://breathe-esg-r57s.vercel.app",
]


# ========================
# REST FRAMEWORK
# ========================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
    ]
}
