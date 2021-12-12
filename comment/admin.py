from django.contrib import admin
from . models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display=['comments', 'added_date']

# Register your models here.
admin.site.register(Comment,CommentAdmin)  