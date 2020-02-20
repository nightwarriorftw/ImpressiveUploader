from django.urls import path
from .views import UploadFileAPIView


app_name = 'api'
urlpatterns = [
    path('upload/', UploadFileAPIView.as_view(), name="upload"),
]
