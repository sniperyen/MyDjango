#coding:utf-8
from django.conf.urls import url,patterns
from django.views.generic import TemplateView
from views import *

urlpatterns=patterns(
    "",
    url(r"^login/", login, name="login"),
    url(r"^logout/", logout, name="logout"),
    url(r"^forget_pwd/", forget_pwd, name="forget_pwd"),
    url(r"^check_reg_info/", check_reg_info, name="check_reg_info"),
    url(r"^register/", register, name="register"),
)

