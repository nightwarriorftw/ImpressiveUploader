import time, os, json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser

from django.http import HttpResponse

from .serializers import UploadFileSerializer

from uploader.forms import UploadFileForm
from uploader.utils import handle_upload

from impressiveUploader.settings import MEDIA_ROOT


class UploadFileAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload(request.FILES['file'])
            return Response({"details":"uploaded successfully", "status": "200_OK"}, status=status.HTTP_200_OK)
        else:
            return Response({"details": "File Uploaded"})
