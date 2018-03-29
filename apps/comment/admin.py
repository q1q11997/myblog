# Register your models here.
from django.contrib import admin
from apps.comment.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','comment_text','comment_time','agree')

admin.site.register(Comment,CommentAdmin)