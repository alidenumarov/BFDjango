from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('add_blog', views.add_block, name="add_blog"),
]