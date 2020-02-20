from django.urls import path
from .views import upload_file


app_name = 'uploader'

urlpatterns = [
    path('', upload_file, name='uploadFile'),
]
