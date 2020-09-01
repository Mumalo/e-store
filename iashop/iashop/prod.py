
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

STATIC_URL = 'https://iastore.com.ng/iashop/public/static/'

STATIC_ROOT = '/home/iastorec/public_html/iashop/public/static/'

MEDIA_URL = 'https://iastore.com.ng/iashop/media/'
#
MEDIA_ROOT = '/home/iastorec/public_html/iashop/media/'
#
# CKEDITOR_UPLOAD_PATH = 'uploads/'