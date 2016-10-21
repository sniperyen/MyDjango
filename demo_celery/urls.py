#coding:utf-8
from django.conf.urls import url,patterns
from django.views.generic import TemplateView
from views import *


urlpatterns=patterns(
    "",
    url(r"^add_task$", AddTask.as_view(), name="add_task"),
)

