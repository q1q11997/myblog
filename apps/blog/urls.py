from django.urls import include,path
from apps.blog import views


urlpatterns = [
    path('<int:blog_id>/', views.blog_each, name='blog_each'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_type/<int:blog_type_id>', views.blog_type, name='blog_type'),
    path('blog_date/<int:year>/<int:month>',views.blog_by_date,name='blog_by_date')
]
