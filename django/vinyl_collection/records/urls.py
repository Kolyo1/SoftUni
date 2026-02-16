from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('add/', views.album_create, name='album_create'),
    path('<int:pk>/', views.album_detail, name='album_detail'),
    path('<int:pk>/edit/', views.album_update, name='album_update'),
    path('<int:pk>/delete/', views.album_delete, name='album_delete'),
]