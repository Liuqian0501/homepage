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
import time
import multiprocessing

def run_function(args):
    return args[1], rundeeplearning(args[0],args[1])

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
            styles = {}
            for key in ['radios_1', 'radios_2', 'radios_3', 'radios_4', 'radios_5', 'radios_6']:
                style =  request.POST.get(key, '')
                if not style == '':
                    styles[key] = style

            style_img = []
            now = time.localtime()
            style_img.append('images/artist/{}{}{}{}content.jpg'.format(now[1], now[2], now[3], now[4]))
            tasks_args = [(img, styles[key]) for key in styles.keys()]
            cores = multiprocessing.cpu_count() 
            pool = multiprocessing.Pool(processes=cores)

            for sty, s_img in pool.imap(run_function, tasks_args):
                with default_storage.open(BASE_DIR + 'content{}.jpg'.format(sty), 'wb+') as destination:
                    for chunk in img.chunks():
                        destination.write(chunk)

                s_img.save(BASE_DIR + 'style{}.jpg'.format(sty))
                style_img.append('images/artist/style{}.jpg'.format(sty))

            pool.close()
            del pool

            
        except Exception as e:
            print(e)
            return  render(request, 'artistpainting/basic.html', {})

        return render(request, 'artistpainting/basic.html', {'style_img': style_img})

    if request.method == 'GET':
        return render(request, 'artistpainting/basic.html', {})



