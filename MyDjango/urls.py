# coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # 静态文件映射（测试用，正式勿用）
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^admin/', include(admin.site.urls)),  # 管理后台
    url(r'^setlang/$', 'django.views.i18n.set_language', name='setlang'),  # 全局语言设置


    url(r'^demo_celery/', include('demo_celery.urls'), name='demo_celery'),  # 定时任务
    url(r'^demo_bootstrap/', include('demo_bootstrap.urls'), name='demo_bootstrap'),  # 基于bootstrap的测试app
)
