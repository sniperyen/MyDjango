#coding:utf-8
from django.conf.urls import url,patterns
from django.views.generic import TemplateView
from views import *

urlpatterns=patterns(
    "",
    url(r"^$", HomePageView.as_view(), name="index"),
)

