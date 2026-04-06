from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def custom_403(request, exception):
    return render(request, '403.html', status=403)

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

handler403 = custom_403
handler404 = custom_404
handler500 = custom_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('users.urls')),
    path('albums/', include('records.urls')),
    path('artists/', include('artists.urls')),
    path('wishlist/', include('wishlist.urls')),
]
