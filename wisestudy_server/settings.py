import datetime
from datetime import timedelta
from django.conf import settings
# from rest_framework.settings import APISettings
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$ql8e$@ahpr1nmgg^bsbbznp!d9od@)#t*h0l6i18mhmd0p%!$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wisestudy_app',
    'rest_framework',
    'drf_yasg',

    # 'rest_framework.authtoken',
    # 'rest_auth',
    #
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'rest_auth.registration',
    #
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.kakao',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wisestudy_server.urls'

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

WSGI_APPLICATION = 'wisestudy_server.wsgi.application'

# 여기 주석처리 안했었네
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.TokenAuthentication',
    ],
}

# JWT_AUTH = {
#     # 'JWT_ENCODE_HANDLER':
#     # 'rest_framework_jwt.utils.jwt_encode_handler',
#     #
#     # 'JWT_DECODE_HANDLER':
#     # 'rest_framework_jwt.utils.jwt_decode_handler',
#     #
#     # 'JWT_PAYLOAD_HANDLER':
#     # 'rest_framework_jwt.utils.jwt_payload_handler',
#     #
#     # 'JWT_PAYLOAD_GET_USER_ID_HANDLER':
#     # 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
#     #
#     # 'JWT_RESPONSE_PAYLOAD_HANDLER':
#     # 'rest_framework_jwt.utils.jwt_response_payload_handler',
#     #
#     # 'JWT_SECRET_KEY': settings.SECRET_KEY,
#     # 'JWT_GET_USER_SECRET_KEY': None,
#     # 'JWT_PUBLIC_KEY': None,
#     # 'JWT_PRIVATE_KEY': None,
#     # 'JWT_ALGORITHM': 'HS256',
#     # 'JWT_VERIFY': True,
#     # 'JWT_VERIFY_EXPIRATION': True,
#     # 'JWT_LEEWAY': 0,
#     # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
#     # 'JWT_AUDIENCE': None,
#     # 'JWT_ISSUER': None,
#     #
#     # 'JWT_ALLOW_REFRESH': True,
#     # 'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
#     #
#     # 'JWT_AUTH_HEADER_PREFIX': 'JWT',
#     # 'JWT_AUTH_COOKIE': None,
#
#     'JWT_SECRET_KEY': settings.SECRET_KEY,
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
#
# }

# REST_USE_JWT = True
#
# SITE_ID = 1
#
# SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
# SOCIALACCOUNT_EMAIL_REQUIRED = False
# SOCIALACCOUNT_QUERY_EMAIL = True


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wisestudy',
        'USER': 'wisestudy',
        'PASSWORD': 'wise$tudy',
        'HOST': '192.168.99.100',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
    
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# URL 마지막 Slash('/') 사용 설정 해제
APPEND_SLASH = False


# SWAGGER_SETTINGS = {
#    'DEFAULT_AUTO_SCHEMA_CLASS': 'wisestudy_server.CamelCaseOperationIDAutoSchema'
# }
