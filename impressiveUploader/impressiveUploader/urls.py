from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("uploader.urls", namespace='uploader')),
    path('api/', include("uploader.api.urls", namespace="api")),
]
