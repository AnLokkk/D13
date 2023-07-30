from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


def nullfy_rating(modeladmin,request, queryset):
    queryset.update(rating=0)
nullfy_rating.short_description = 'reset rating'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateCreation', 'rating',)
    list_filter = ('postCategory',)
    search_fields = ('title',)
    actions = [nullfy_rating]

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
