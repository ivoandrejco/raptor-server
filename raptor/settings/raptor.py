
import os 

STATIC_ROOT= os.environ['STATIC_ROOT']
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    },
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'raptor2',
        'USER': os.environ['DEFAULT_DB_USER'],
        'PASSWORD': os.environ['DEFAULT_DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}


