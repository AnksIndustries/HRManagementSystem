import os
from decouple import config, Csv

ENVIRONMENT='DEVELOPMENT'
SECRET_KEY='3q*=5%_@6#(d!4$o=-2$3=gf0!*6tt*_@d-u_&-+_s@w35*-_x'

DJANGO_TEMPLATE_DEBUG='yes'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = SECRET_KEY
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

SOLITONEMS_APPS = [
    'recruitment',
    'employees',
    'payroll',
    'leave',
    'organisation_details',
    'settings',
    'overtime',
    'holidays',
    'ems_auth',
    'ems_admin',
    'contracts',
    'learning_and_development',
    'training',
    'notification',
    'performance'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'javascript_settings',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = SOLITONEMS_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SOLITONEMS.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'SOLITONEMS.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'ems_auth.User'

AUTHENTICATION_BACKENDS = ['ems_auth.backends.EmailBackend']

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ankit.see@gmail.com'
EMAIL_HOST_PASSWORD = 'Security_1998'
FROM_EMAIL = 'ankit.see@gmail.com'
DEFAULT_FROM_EMAIL = 'ankit.see@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
