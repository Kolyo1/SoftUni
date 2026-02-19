from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_list, name='wishlist_list'),
    path('add/', views.wishlist_create, name='wishlist_create'),
    path('delete/<int:pk>/', views.wishlist_delete, name='wishlist_delete'),
    path('move-to-collection/<int:pk>/', views.move_to_collection, name='move_to_collection'),
]