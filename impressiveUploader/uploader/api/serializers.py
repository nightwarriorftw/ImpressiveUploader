from rest_framework import serializers
from uploader.models import UploadFileModel

class UploadFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UploadFileModel
        fields = ['name', 'type', 'file']
