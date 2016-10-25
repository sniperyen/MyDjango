from django.conf.urls import patterns, url, include
from rest_framework import routers
from demo_restfulapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.ArticleViewSet)
