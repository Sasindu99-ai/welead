import os
from pathlib import Path
from typing import List

BASE_DIR = Path(os.environ.get("DJANGO_SETTINGS_BASE_PATH", ".")).resolve()
DEBUG = os.environ.get("DEBUG", "True") == "T"
SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key")
ENV = os.environ.get("ENVIRONMENT", "development")
USE_TZ = True

if "INSTALLED_APPS" not in globals():
    INSTALLED_APPS: List[str] = []

INSTALLED_APPS = (
    [
        "apps.authentication.apps.AuthenticationConfig",
        "apps.main.apps.MainConfig",
        "apps.settings.apps.SettingsConfig",
    ]
    + INSTALLED_APPS
    + [
        "django.contrib.sites",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.google",
        "allauth.socialaccount.providers.apple",
    ]
)

if "MIDDLEWARE" not in globals():
    MIDDLEWARE: List[str] = []

MIDDLEWARE += [
    "allauth.account.middleware.AccountMiddleware",
]

DATABASE = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': os.environ.get('DB_SCHEMA', 'viptravels_db'),
    #     'USER': os.environ.get('DB_USERNAME', 'root'),
    #     'PASSWORD': os.environ.get('DB_PASSWORD', ''),
    #     'HOST': os.environ.get('DB_HOST', 'localhost'),
    #     'PORT': os.environ.get('DB_PORT', '3306'),
    # }
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if "TEMPLATES" not in globals():
    TEMPLATES: list = [{"DIRS": []}]

TEMPLATES[0]["DIRS"] += [BASE_DIR / "static/templates"]

# AUTHENTICATION_BACKENDS += [
# 	'django.contrib.auth.backends.ModelBackend',
# 	'allauth.account.auth_backends.AuthenticationBackend',
# ]

AUTH_USER_MODEL = "authentication.User"

SITE_ID = 2

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "email",
            "profile",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_ADAPTER = "apps.authentication.adapters.SocialAccountAdapter"
LOGIN_REDIRECT_URL = "http://localhost:8008/auth/social/login/redirect/"

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"  # noqa F405

# Media files (Images)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"  # noqa F405

# SMTP Configuration
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # Development
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # Production
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

APPEND_SLASH = True

if "JAZZMIN_SETTINGS" not in globals():
    JAZZMIN_SETTINGS = {}

JAZZMIN_SETTINGS["site_title"] = "Welead Admin"
JAZZMIN_SETTINGS["site_header"] = "Welead"
JAZZMIN_SETTINGS["site_brand"] = "Welead"
JAZZMIN_SETTINGS["welcome_sign"] = "Welcome to Welead Admin"
JAZZMIN_SETTINGS["icons"] = {
    "auth": "fas fa-users-cog",
    "auth.group": "fas fa-users",
    "authentication": "fas fa-users-cog",
    "authentication.user": "fas fa-user",
    "account.emailaddress": "fas fa-at",
    "authtoken.tokenproxy": "fas fa-key",
    "settings.country": "fas fa-flag",
    "settings.currency": "fas fa-dollar-sign",
    "settings.page": "fas fa-file",
    "settings.place": "fas fa-map-marker-alt",
    "settings.setting": "fas fa-cogs",
    "sites.site": "fas fa-globe",
    "socialaccount.socialaccount": "fas fa-user",
    "socialaccount.socialtoken": "fas fa-key",
    "socialaccount.socialapp": "fas fa-user",
}
