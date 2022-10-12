from django.db import models

from innotter import settings


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "tags"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=80)
    uuid = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='pages')

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