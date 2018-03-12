from django.urls import include,path
from apps.index import views


urlpatterns = [
    path('',views.index,name='index'),
    path('search/', views.search, name='search'),
    path('new_index/',views.new_index,name='new_index'),
    path('Carousel/',views.Carousel, name='Carousel'),
]