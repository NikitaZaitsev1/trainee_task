from typing import List
from uuid import uuid4

from django.db import models

from innotter import settings
from page.models import Page


class Post(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid4, editable=False)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=180)
    reply_to = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.content


class Like(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid4, editable=False)
    like_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    value = models.IntegerField(default=1, editable=False)

    class Meta:
        db_table = "likes"


class Comment(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('Comment', null=True, blank=True, related_name='replies', on_delete=models.SET_NULL)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.text
