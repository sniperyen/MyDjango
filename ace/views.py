# coding=utf-8
import logging
import datetime
import uuid

from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import TemplateView

__author__ = 'sanyang'


class HomePageView(TemplateView):
    template_name = 'ace/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context


class DomainView(TemplateView):
    template_name = 'ace/domain_list.html'

    def get_context_data(self, **kwargs):
        context = super(DomainView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context
