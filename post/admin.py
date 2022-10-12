from django.contrib import admin

from post.models import Post


class AdminPost(admin.ModelAdmin):
    list_display = ('page', 'content', 'created_at', 'updated_at')
    list_filter = ('page', 'created_at')


admin.site.register(Post, AdminPost)
