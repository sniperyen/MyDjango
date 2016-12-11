from rest_framework import serializers
from .models import User, Article
from ace.models import Node


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ('title', 'body', 'created_at', 'status', 'author')


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('node_name', 'node_type', 'node_address', 'node_contact', 'node_signer', 'node_remarks', 'node_signtime')


