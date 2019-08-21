from django.shortcuts import render
from .models import UploadedImages
import face_recognition
import numpy as np
import hashlib
from PIL import Image

def home(request):
    ctx = {}
    return render(request, 'fdx_search/index.html',ctx)

def search_error(request,err):
    ctx = {}
    return render(request, 'fdx_search/search_error.html',ctx)

def search(request):
    ctx = {}
    if request.FILES['file'].size == 0:
        return search_error(request,"Плохой файл")
    hasher = hashlib.md5()
    for chunk in request.FILES['file'].chunks():
           hasher.update(chunk)
    file_md5 = hasher.hexdigest()
    #-----
    try:
        im = Image.open(request.FILES['file'])
        (width, height) = im.size
    except:
        return search_error(request,"Плохая картинка")
    #-----
    ctx['file_md5'] = file_md5
    ctx['width'] = width
    ctx['height'] = height
    ui = UploadedImages()
    ui.file = request.FILES['file']
    ui.md5 = file_md5
    ui.width = width
    ui.height = height
    ui.save()
    return render(request, 'fdx_search/search.html',ctx)

def search1(request,slug11):
    ctx = {}
    return render(request, 'fdx_search/search.html',ctx)

def search2(request,slug11,slug22):
    ctx = {}
    return render(request, 'fdx_search/search.html',ctx)