"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '51nf8!s8+wrc%*mpgcb62-l6!!0nvt*@wbp_$j4&aos282fe^z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if 'DYNO' in os.environ:  # Running on Heroku
    DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # 管理者後台
    'django.contrib.auth',  # 認證授權管理
    'django.contrib.contenttypes',  # 內容類型管理
    'django.contrib.sessions',  # session 管理
    'django.contrib.messages',  # 訊息管理
    'django.contrib.staticfiles',  # 靜態檔案管理
    'account',
    'article',
    'upload_profile',
    'main',
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

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG:  # Running on the development environment
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'blogdb',
            'USER': 'blog',
            'PASSWORD': 'blog',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:  # Running on Heroku
    # Parse database configuration from $DATABASE_URL
    import dj_database_url

    DATABASES = {'default': dj_database_url.config()}
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
AUTH_USER_MODEL = 'account.User'

MEDIA_URL = '/main/media/'  # 訪問文件的URL根目錄
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 上傳文件儲存根目錄
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/account/login/'

# For Heroku deployment
# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# STATICFILES_DIRS = (
#    ('css',os.path.join(STATIC_ROOT,'css')).replace('\\','/'),
#    ('js',os.path.join(STATIC_ROOT,'js'))).replace('\\','/'),
#    ('images',os.path.join(STATIC_ROOT,'images'))).replace('\\','/'),
#    ('upload',os.path.join(STATIC_ROOT,'upload')).replace('\\','/'),
# )
