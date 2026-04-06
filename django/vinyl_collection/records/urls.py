from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='album_list'),
    path('add/', views.AlbumCreateView.as_view(), name='album_create'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
]
