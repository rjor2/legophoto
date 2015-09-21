from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadImageForm
from django.template import RequestContext

from photo.models import Image

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger("default")

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def upload_image(request):
    if request.method == 'POST':
        logger.debug('post')
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            logger.debug('valid')

            image = Image(docfile=request.FILES['file'])
            image.save()
            # return HttpResponseRedirect('/success/url/')
            render_to_response('photo/upload.html', {'form': form, 'msg': "File Uploaded"})

        else:
            logger.debug('invalid')

    else:
        logger.debug('get')
        form = UploadImageForm()
    return render_to_response(
        'photo/upload.html',
        {'form': form, 'msg': "File Uploaded"},
        context_instance=RequestContext(request))
