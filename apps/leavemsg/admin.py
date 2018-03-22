from django.contrib import admin
from .models import LeaveMsg
# Register your models here.
@admin.register(LeaveMsg)
class LeaveMsgAdmin(admin.ModelAdmin):
    list_display = ('msg','time')