from django.contrib import admin
from apps.index.models import Music

# Register your models here.

@admin.register(Music)
class Music(admin.ModelAdmin):
    list_display = ('music_name','singer','music_word','music_id')

