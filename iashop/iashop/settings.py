"""
Django settings for iashop project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .secret import DATABASE_NAME, PASSWORD, USER, SECRET_KEY, EMAIL_HOST, \
    EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS, HOST, ENGINE
from django.core.urlresolvers import reverse_lazy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'material',
    'material.frontend',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    # 'bootstrap3',
     # 'jquery',
    # 'staticfiles_select2',
    # 'smart_selects',
    'common',
    # 'shop',
    'account',
    'base',
    'auction',
    'cart',
    # 'selectable',
    # 'selectable_select2',
    # 'notify',
    'smart_selects',
    'notifications',
)


SELECTABLE_ESCAPED_KEYS = ('label', 'value')


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'iashop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                 'django.core.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# TEMPLATE_CONTEXT_PROCESSORS += ("django.core.context_processors.request",)

CATEGORY_SESSION_ID = 'c_name'
CART_SESSION_ID = 'cart'


USE_DJANGO_JQUERY = True


WSGI_APPLICATION = 'iashop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
#     'select2': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# SELECT2_CACHE_BACKEND = 'select2'


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': ENGINE,
        'NAME': DATABASE_NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        # 'PORT': '',
    }

}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/



STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'shop/static'),
)

# print(STATICFILES_DIRS)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('accounts:user_detail',
    args=[u.id])
}


NOTIFICATIONS_SOFT_DELETE=True
NOTIFICATIONS_USE_JSONFIELD=True
# Notify settings

# NOTIFY_SOFT_DELETE = True
# NOTIFY_NF_LIST_CLASS_SELECTOR = '.notifications'
#
# NOTIFY_NF_BOX_CLASS_SELECTOR = '.notification-box-list'
#
# NOTIFY_MARK_NF_CLASS_SELECTOR = '.mark-notification'
# NOTIFY_MARK_ALL_NF_CLASS_SELECTOR = '.mark-all-notifications'
# NOTIFY_READ_NOTIFICATION_CSS = 'read'
# NOTIFY_UNREAD_NOTIFICATION_CSS = 'unread'
#
# NOTIFY_DELETE_NF_CLASS_SELECTOR = '.delete-notification'
# NOTIFY_UPDATE_TIME_INTERVAL = ''


# Email settings

EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT
EMAIL_USE_TLS = EMAIL_USE_TLS



LOGIN_URL = reverse_lazy('accounts:login')
LOGOUT_URL = reverse_lazy('accounts:logout')