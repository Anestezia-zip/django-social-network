from django.contrib import admin
from .models import Post, Region

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated', 'author')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')