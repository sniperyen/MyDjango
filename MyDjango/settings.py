# coding=utf-8
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'z*#yeb0$qt0r!$q+^jzd2rs3#xiefty*gs!%2n2(=b!5)129kf'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    # 内置应用
    # 'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 第三方应用
    'debug_toolbar',  # 调试工具
    'reversion',
    'djcelery',  # 定时
    'Lib.bootstrap3',  # 样式
    'Lib.crispy_forms',  # 模板定义  http://django-crispy-forms.readthedocs.io/en/latest/
    'xadmin',  # 后台管理 https://github.com/sshwsfc/xadmin

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# region Settings for Internationalization
LANGUAGES_SUPPORTED = ('en-us', 'zh-cn',)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True  # 国际化 -- Internationalization，i 和 n 之间有 18 个字母，简称 I18N
USE_L10N = True  # 本地化 -- localization， l 和 n 之间有 10 个字母，简称 L10N
USE_TZ = True
# endregion

# region Setting for (JS/CSS/IMAGE/TEMPLATE)
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
# endregion

# region Settings for django-bootstrap3
BOOTSTRAP3 = {
    'set_required': False,
    'error_css_class': 'bootstrap3-error',
    'required_css_class': 'bootstrap3-required',
    'javascript_in_head': True,
    'jquery_url': os.path.join(STATIC_URL, 'js/jquery.min.js'),
    'base_url': os.path.join(STATIC_URL, 'bootstrap/'),
}
# endregion

# region Settings for celery
import djcelery

djcelery.setup_loader()

BROKER_URL = 'amqp://guest:guest@127.0.0.1:5672//'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERY_TIMEZONE = TIME_ZONE  # 使用和Django一样的时区
# endregion

# region Settings for log
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

# endregion
