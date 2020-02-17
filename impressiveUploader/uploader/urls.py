from django.urls import path
from .views import uploadFileView


app_name = 'uploader'

urlpatterns = [
    path('', uploadFileView, name='uploadFile'),
]