from django.urls import path
from apps.comment import views


urlpatterns = [
    path('post_comment', views.PostComment, name='post_comment'),
]
