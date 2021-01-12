from django.contrib import admin

from website.models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "sub_title", "categories", "approved"]
    search_fields = ["title", "sub_title"]


admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
