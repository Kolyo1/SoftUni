from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('users.urls')),
    path('albums/', include('records.urls')),
    path('artists/', include('artists.urls')),
    path('wishlist/', include('wishlist.urls')),
]
