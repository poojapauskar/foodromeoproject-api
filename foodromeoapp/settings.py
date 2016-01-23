"""
Django settings for foodromeoapp project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'poojapauskar22'
EMAIL_HOST_PASSWORD = 'pooja22222'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1@@u-q$6yv7*1mx7=(=^mzj!qgqrjb=@!mpai8*d=wn1#cx9e7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# WSGIPassAuthorization ="On"
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'register',
    'verify',
    'social.apps.django_app.default',
    'facebook',
    'google',
    'oauth2_provider',
)

AUTH_PROFILE_MODULE = 'profiles.profile'

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

ROOT_URLCONF = 'foodromeoapp.urls'

# FIELDS_STORED_IN_SESSION = ['key']
# LOGIN_REDIRECT_URL = '/'

# SOCIAL_AUTH_FACEBOOK_KEY = '177909892570210'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'db005a2d32b03896dd46341e8cba2081'

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', # needed starting from protocol v2.4
}

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email'] 



FACEBOOK_APP_ID = '177909892570210'
FACEBOOK_SECRET_KEY = 'db005a2d32b03896dd46341e8cba2081'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '219221435680-f4oiivqg1mil18deh9dm0e2kvpisc9j4.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '2GPU8BEZi5HNMkyybsC38xNd'

# SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
# TEMPLATE_DIRS = (       
#                   os.path.join(SETTINGS_PATH, 'templates'),
#                   os.path.join(SETTINGS_PATH, 'templates/foodromeoapp')

# )

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
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]



AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'foodromeoapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddus0gocf25n4p',                      
        'USER': 'gfunckdkjmeebp',
        'PASSWORD': 'ZysX_MRBc053Xh_D7G8nUNSXX-',
        'HOST': 'ec2-107-21-120-109.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if os.environ.get('DATABASE_URL', None):
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()


DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_URL = '/static/'
