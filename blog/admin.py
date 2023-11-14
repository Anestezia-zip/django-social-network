from django.contrib import admin
from .models import Post, Region, UserProfile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated', 'author')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(UserProfile)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('avatar', 'bio')