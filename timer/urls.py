# coding:utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import *

__author__ = 'sanyang'

urlpatterns = patterns('',
                       url('^$', index),
                       url('^(\d*)$', TemplateView.as_view(template_name='page.html'), ),
                       (r'^test1_view$', test1_view),
)