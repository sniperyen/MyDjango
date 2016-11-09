# coding=utf-8
import logging
import datetime
import uuid

from django.contrib import auth
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.template import RequestContext

from django.contrib.auth.models import User
from models import MyProfile
from forms import UserForm

__author__ = 'sanyang'


def login(request):
    if request.method == 'POST':
        next = request.POST.get("next", '/')
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return RedirectView.as_view(url="/")(request)
            else:
                form.errors['msg'] = '用户名或密码不正确'
    else:
        next = request.GET.get('next', '/')
        form = UserForm()
    return render_to_response('customer/login.html', {'form': form, 'next': next},
                              context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    next = reverse('customer:login')
    return HttpResponseRedirect(next)
