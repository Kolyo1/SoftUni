from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, ArtistViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
