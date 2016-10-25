# coding=utf-8
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    class Meta:
        db_table = 'user'

class Article(models.Model):
    STATUS_SET = (
            (0, "草稿"),
            (1, "公开"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_SET, default=0)
    author = models.ForeignKey(User, related_name='entries')

    class Meta:
        db_table = 'article'