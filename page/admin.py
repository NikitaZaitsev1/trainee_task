from django.contrib import admin

from page.models import Page, Tag


class AdminPage(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_private', 'unblock_date')
    list_filter = ('name', 'owner', 'is_private')


admin.site.register(Page, AdminPage)


class AdminTags(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Tag, AdminTags)
