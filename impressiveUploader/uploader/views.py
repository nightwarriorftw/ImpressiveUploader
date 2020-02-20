from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import UploadFileForm
from .utils import handle_upload


# View that handles uploading big files
def upload_file(request):
    form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
 