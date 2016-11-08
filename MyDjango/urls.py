# coding=utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from demo_restfulapi.urls import router

# from django.contrib import admin
# admin.autodiscover()

import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^setlang/$', 'django.views.i18n.set_language', name='setlang'),  # 全局语言设置
    url(r'^admin/', include(xadmin.site.urls)),  # # 后台管理模块

    url(r'^$', include('ace.urls'), name="ace"),
    url(r'^demo_celery/', include('demo_celery.urls'), name='demo_celery'),  # 定时任务
    url(r'^demo_bootstrap/', include('demo_bootstrap.urls'), name='demo_bootstrap'),  # 基于bootstrap的测试app

    # restfulapi
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)