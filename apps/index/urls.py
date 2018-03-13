from django.urls import include,path
from apps.index import views


urlpatterns = [
    path('',views.index,name='index'),
    path('search/', views.search, name='search'),
    path('Carousel/',views.Carousel, name='Carousel'),
]