from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from google.cloud import storage


import io
import os
import json
from .src.load_model import rundeeplearning
import base64
from PIL import Image
import numpy as np
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static-storage/images/artist/'
# Create your views here.
@csrf_exempt
def styleTransform(request):
    """
    style transform service
    """
    if request.method == 'POST':

        try:
            img = request.FILES['image']
            style =  request.POST['radios']
            with default_storage.open(BASE_DIR + 'content.jpg', 'wb+') as destination:
                for chunk in img.chunks():
                    destination.write(chunk)

            img_out = rundeeplearning(img, style)
            img_out.save(BASE_DIR + 'style.jpg')
            
        except KeyError:
            return  render(request, 'artistpainting/basic.html', {})

        return render(request, 'artistpainting/basic.html', {'src1': 'images/artist/style.jpg',
                                                            'src2': 'images/artist/content.jpg'})

    if request.method == 'GET':
        return render(request, 'artistpainting/basic.html', {})



