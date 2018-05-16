from django.urls import path
from apps.space import views
urlpatterns = [
    path('<int:user_id>/',views.space,name='space'),
]