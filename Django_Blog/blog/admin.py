from django.contrib import admin
from .models import Author,Blog,Comment
# Register your models here.
admin.site.register(Author)

class CommentInline(admin.TabularInline):
    model = Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_description','created_at']
    
    def get_description(self,object):
        return object.comment_content[:75]

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CommentInline]

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)