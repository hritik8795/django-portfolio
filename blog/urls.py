from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home_blog,name="home_blog"),
    path('<int:blog_id>/',views.detail, name='detail')
]