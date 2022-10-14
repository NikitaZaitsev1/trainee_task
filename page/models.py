from uuid import uuid4

from django.db import models

from innotter import settings


class Tag(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "tags"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=80)
    uuid = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid4, editable=False)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='pages', blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pages')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follows')

    image = models.URLField(null=True, blank=True)

    is_private = models.BooleanField(default=False)
    follow_requests = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='requests')

    unblock_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "pages"
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.name
