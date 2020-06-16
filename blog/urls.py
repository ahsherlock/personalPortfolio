from django.contrib import admin
from django.urls import path, include
from . import views

#set equal to name of application
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]