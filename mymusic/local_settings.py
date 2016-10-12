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
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.views.jwt_response_payload_handler',
}



AUTHENTICATION_BACKENDS = (
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


FACEBOOK_APP_ID              = '353258371678607'
FACEBOOK_API_SECRET          = '53b3d718fc8908561e7b57ade780ad5e'


LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'