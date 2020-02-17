from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import UploadForm
from .utils import handle_upload


def uploadFileView(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload(request.FILES['file'])
            return JsonResponse({"message": "success"})
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})
