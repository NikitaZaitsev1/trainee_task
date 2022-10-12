from django.contrib import admin

from user.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ('role', 'email', 'title', 'is_blocked')
    list_filter = ('role', 'title', 'is_blocked')


admin.site.register(User, AdminUser)
