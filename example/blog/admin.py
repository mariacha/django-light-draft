# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin
from light_draft.admin import DraftAdmin

from .models import BlogPost, TextBlock, Tag


class TextBlockInline(admin.TabularInline):
    model = TextBlock
    extra = 1


class BlogPostAdmin(DraftAdmin):
    list_display = ('title', 'category',)
    fields = ('title', 'category', 'tags', 'lead', 'body')
    list_select_related = ('category',)
    inlines = [TextBlockInline]
    filter_horizontal = ('tags',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register([Tag])
