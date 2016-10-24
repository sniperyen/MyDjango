# coding=utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

# from django.contrib import admin
# admin.autodiscover()

import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns(
    '',
    # 静态文件映射（测试用，正式勿用）
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(xadmin.site.urls)),  # # 后台管理模块

    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^demo_celery/', include('demo_celery.urls'), name='demo_celery'),  # 定时任务
    url(r'^demo_bootstrap/', include('demo_bootstrap.urls'), name='demo_bootstrap'),  # 基于bootstrap的测试app
    url(r'^setlang/$', 'django.views.i18n.set_language', name='setlang'),  # 全局语言设置
)