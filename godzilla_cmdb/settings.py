"""
Django settings for godzilla_cmdb project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sa87blgn%47f-rn%mo(4188$%o0v3wvt9br02d9&^x^1i2$)eu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'godzilla.apps.GodzillaConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES = (

  # 'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
)


ROOT_URLCONF = 'godzilla_cmdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'godzilla_cmdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT':'3306',
    }
}





# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/godzilla/static/'
STATICFILES_DIRS = (
    os.path.join(os.path.join(BASE_DIR, 'godzilla/static')),
)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')



LOGIN_URL = '/godzilla/login'

SESSION_COOKIE_NAME = "sessionid"      # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）

SESSION_COOKIE_PATH = "/"              # Session的cookie保存的路径（默认）

SESSION_COOKIE_DOMAIN = None             # Session的cookie保存的域名（默认）

SESSION_COOKIE_SECURE = False          # 是否Https传输cookie（默认）

SESSION_COOKIE_HTTPONLY = True         # 是否Session的cookie只支持http传输（默认）

SESSION_COOKIE_AGE = 18000             # Session的cookie失效日期（2周）（默认）

SESSION_EXPIRE_AT_BROWSER_CLOSE = True    # 是否关闭浏览器使得Session过期（默认）

SESSION_SAVE_EVERY_REQUEST = True        # 是否每次请求都保存Session，默认修改之后才保存（默认）

APPEND_SLASH=False

AUTH_USER_MODEL = 'godzilla.users'

# WEBSOCKET_ACCEPT_ALL=True

