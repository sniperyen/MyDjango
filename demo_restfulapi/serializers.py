from rest_framework import serializers
from .models import User, Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ('title', 'body', 'created_at', 'status', 'author')
