from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'ratingAuthor')
    list_filter = ('authorUser', 'ratingAuthor',)
    search_fields = ('authorUser',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'author', 'categoryType', 'rating')
    list_filter = ('dateCreation', 'author', 'categoryType', 'rating')
    search_fields = ('author',)


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('postThrough', 'categoryThrough')
    list_filter = ('categoryThrough',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentPost', 'commentUser', 'rating')
    list_filter = ('commentUser', 'rating')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
