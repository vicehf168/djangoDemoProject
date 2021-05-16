"""
Django settings for demoproject project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#path.resolve()方法，返回当前脚本的绝对路径，parent则获取父路径，settings的父目录是demoapp，再上一层父目录是demoproject
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fenahzi8!-#t+v^0o5^e!3u)b==mh2mt1wq0lrp@=bc5k!^_8f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]


CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

ROOT_URLCONF = 'demoproject.urls'

ALLOWED_HOSTS = ['*']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #DIRS加载html文件的路径，views中读取html文件都在这个路径下找，该方法蒋BASE_DIR和templates拼接成一个完成整路径
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'demoproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# 多数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'flabordb': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kuname',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': '3306',
        },
    'eplatformdb': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kuname',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': '3306',
        },
    'corecontractdb': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kuname',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': '3306',
        },
    'corebilldb': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kuname',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': '3306',
        },
    'humanrundb': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kuname',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': '3306',
        }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 配置数据库路由
DATABASE_ROUTERS = ['demoproject.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    'flaborapp': 'flabordb',
    'eplatformapp': 'eplatformdb',
    'corecontractapp': 'corecontractdb',
    'corebillapp': 'corebilldb',
    'humanrunapp': 'humanrundb',
}
