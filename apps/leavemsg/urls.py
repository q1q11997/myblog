from django.urls import include,path
from .views import *


urlpatterns = [
    path('leave_view',leave_view,name='leave_view')
]
