from django.contrib import admin

from page.models import Page, Tag


class AdminPage(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_private', 'unblock_date', 'is_blocked')
    list_filter = ('name', 'owner', 'is_private','is_blocked')


admin.site.register(Page, AdminPage)


class AdminTags(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Tag, AdminTags)
