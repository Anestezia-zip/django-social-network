from django.contrib import admin
from .models import Post

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated', 'author')
    prepopulated_fields = {'slug': ('title',)}
