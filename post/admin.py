from django.contrib import admin

from post.models import Post, Comment


class AdminPost(admin.ModelAdmin):
    list_display = ('page', 'content', 'created_at', 'updated_at')
    list_filter = ('page', 'created_at')


class AdminComment(admin.ModelAdmin):
    list_display = ('date_added', 'text')
    list_filter = ('date_added', 'text')


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
