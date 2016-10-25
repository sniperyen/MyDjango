# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import User, Article
from serializers import UserSerializer, ArticleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    filter_fields = ('author', 'status')
