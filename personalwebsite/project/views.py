from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from .models import ContentImage

import io
import os
import json
from .src.trans_model import TransGraph
from .src.recognition_model import predict_app
import base64
from PIL import Image
import numpy as np
import logging
import time

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/static-storage/images/'

def runfuc(args):
    
    # im = Image.open(args[0])

    # print(im)
    s_img  = TransGraph(args[0], args[1]).run()
    # s_img = model.run()
    s_img.save(BASE_DIR + 'artist/style{}.jpg'.format(args[1]))
    style_img = 'images/artist/style{}.jpg'.format(args[1])

    return style_img


# Create your views here.
@csrf_exempt
def styleTransform(request):
    """
    style transform service
    """
    if request.method == 'POST':
        
        style_img_url = []
        try:
            
            # read styles
            styles = {}
            for key in ['radios_1', 'radios_2', 'radios_3', 'radios_4', 'radios_5', 'radios_6']:
                style =  request.POST.get(key, '')
                if not style == '':
                    styles[key] = style

            now = time.localtime()

            # load image
            img = request.FILES['image']
            name = '{}{}{}{}{}content.jpg'.format(now[1], now[2], now[3], now[4], now[5])

            #save to database
            Image = ContentImage()
            Image.name = 'static/images/artist/' + name
            Image.save()
            
            #save to disk
            addr = BASE_DIR + 'artist/' + name
            save_to_disk(addr, img)

            # appento url
            style_img_url.append('images/artist/' + name)
            
            # multiprocessing
            pool = ThreadPool(6) 
            tasks_args = [(addr, styles[key]) for key in styles.keys()]
            style_img_url += pool.map(runfuc, tasks_args)

            
        except Exception as e:
            print(e)
            return  render(request, 'artistpainting/basic.html', {})

        return render(request, 'artistpainting/basic.html', {'style_img': style_img_url})

    if request.method == 'GET':
        return render(request, 'artistpainting/basic.html', {})


# Create your views here.
@csrf_exempt
def recognition(request):
    """
    style transform service
    """
    if request.method == 'POST':
        
        name = ''
        predicitons = ''
        try:
            # load image
            now = time.localtime()
            img = request.FILES['image']
            image_name = '{}{}{}{}{}object.jpg'.format(now[1], now[2], now[3], now[4], now[5])
            
            # get prediction
            predicitons = predict_app(img)
            
            # save to database
            Image = ContentImage()
            Image.name = 'static/images/predict/' + image_name
            Image.save()

            # save to disk
            addr = BASE_DIR + 'predict/' + image_name
            save_to_disk(addr, img)
            image_url = 'images/predict/' + image_name

            
        except Exception as e:
            print(e)
            return  render(request, 'recognition/basic.html', {})

        return render(request, 'recognition/basic.html', {'image_url':image_url, 'predictions': predicitons})

    if request.method == 'GET':
        return render(request, 'recognition/basic.html', {})



def save_to_disk(addr, img):
    with default_storage.open(addr, 'wb+') as destination:
        for chunk in img.chunks():
            destination.write(chunk)

