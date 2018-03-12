from django.contrib import admin
from apps.blog.models import BlogType,Blog

# Register your models here.

@admin.register(BlogType)
class BlogType(admin.ModelAdmin):
    list_display = ('id','type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','blog_type','created_time','last_updated_time','read_num')

