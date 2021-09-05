from django.urls import path

from . import views

app_name = 'posts_urls'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
