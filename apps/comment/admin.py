# Register your models here.
from django.contrib import admin
from apps.comment.models import CommentPost

# Register your models here.
class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('User','Comment','CommentTime','Agree')

admin.site.register(CommentPost,CommentPostAdmin)