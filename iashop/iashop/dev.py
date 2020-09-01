

from .common import *




DEBUG = True
# TEMPLATE_DEBUG = DEBUG

# ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iashop',
        'USER': 'root',
        'PASSWORD': 'mumalo1993',
        'HOST': '',
        'PORT': '',
    }

}
SECRET_KEY = SECRET_KEY

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'