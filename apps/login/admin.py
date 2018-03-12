from django.contrib import admin
from apps.login.models import User
# Register your models here.
class BlogLoginAdmin(admin.ModelAdmin):
    list_display = ('name','email','sex','c_time')

admin.site.register(User,BlogLoginAdmin)