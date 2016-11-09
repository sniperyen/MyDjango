# coding=utf-8
import logging
import datetime
import uuid

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView

from utils.util_web import TemplateViewBase

__author__ = 'sanyang'


class HomePageView(TemplateViewBase):
    template_name = 'ace/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context


class DomainView(TemplateViewBase):
    template_name = 'ace/domain_list.html'

    def get_context_data(self, **kwargs):
        context = super(DomainView, self).get_context_data(**kwargs)
        return context
