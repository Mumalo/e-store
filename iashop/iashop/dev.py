

from .common import *




DEBUG = True
# TEMPLATE_DEBUG = DEBUG

# ALLOWED_HOSTS = ['*']

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

SECRET_KEY = SECRET_KEY

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'
