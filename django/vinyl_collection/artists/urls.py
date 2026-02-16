# artists/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('<int:pk>/', views.artist_detail, name='artist_detail'),
    path('create-artist/', views.artist_create_ajax, name='artist_create_ajax'),
    path('create-genre/', views.genre_create_ajax, name='genre_create_ajax'),
]