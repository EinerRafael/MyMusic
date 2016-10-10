from .constants import *
from datetime import timedelta

"""
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER
    }
}

RQ_QUEUES = {
    'default': {
        'HOST': REDIS_HOST,
        'PORT': REDIS_PORT,
        'DB': 1,
        'DEFAULT_TIMEOUT': 360,
    },
    'low': {
        'HOST': REDIS_HOST,
        'PORT': REDIS_PORT,
        'DB': 1,
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

_REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(days=1),
}

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)


CORS_ORIGIN_WHITELIST = (
    '*',
)

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
)

CORS_URLS_REGEX = r'^/api/.*$'