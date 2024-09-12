from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'content')
    search_fields = ('content',)
    list_filter = ('author', 'created_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

