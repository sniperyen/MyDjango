#coding:utf-8
from django.conf.urls import url,patterns
from django.views.generic import TemplateView
from views import *

urlpatterns=patterns(
    "",
    url(r"^login/", login, name="login"),
    url(r"^logout/", logout, name="logout"),
)

