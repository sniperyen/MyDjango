# coding=utf-8
"""
Django settings for untitled project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z*#yeb0$qt0r!$q+^jzd2rs3#xiefty*gs!%2n2(=b!5)129kf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# celery settings
import djcelery

djcelery.setup_loader()

BROKER_URL = 'amqp://guest:guest@192.168.30.251:5672//'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# Application definition

INSTALLED_APPS = (
    # 内置应用
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 第三方应用
    'debug_toolbar',  # 调试工具
    'bootstrap_toolkit',  # 样式
    'django_admin_bootstrapped',  # admin样式
    'djcelery',  # 定时

    # 测试应用
    'demo_bootstrap',  # bootstrap的一个示例app
    'demo_celery',

    # 公共应用
    'utils',
)

MIDDLEWARE_CLASSES = (
    'MyDjango.middleware.BlockedIpMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'MyDjango.middleware.UserBasedExceptionMiddleware',
)

ROOT_URLCONF = 'MyDjango.urls'

WSGI_APPLICATION = 'MyDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGES_SUPPORTED = ('en-us', 'zh-cn',)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True  # 国际化 -- Internationalization，i 和 n 之间有 18 个字母，简称 I18N

USE_L10N = True  # 本地化 -- localization， l 和 n 之间有 10 个字母，简称 L10N

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# 静态文件访问的设置
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_resources/').replace('\\', '/')  # 开发环境用不到，生产环境才用到
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads").replace('\\', '/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.i18n',
                               'django.contrib.auth.context_processors.auth',
                               )

# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s[line:%(lineno)d] %(levelname)s (%(thread)d) (%(asctime)s) %(message)s',
    datefmt='%H:%M:%S',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#          'require_debug_false': {
#              '()': 'django.utils.log.RequireDebugFalse'
#          }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }