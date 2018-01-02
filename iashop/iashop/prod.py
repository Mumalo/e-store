


from os.path import normpath, join

from .common import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


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

STATIC_URL =  'http://iastore.com.ng/iashop/public/static/'

STATIC_ROOT = '/home/iastorec/public_html/iashop/public/static/'

MEDIA_URL = 'http://iastore.com.ng/iashop/public/media/'

MEDIA_ROOT = '/home/iastorec/public_html/iashop/public/'

CKEDITOR_UPLOAD_PATH = 'uploads/'