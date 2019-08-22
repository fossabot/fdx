from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
    ctx['err'] = err
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
    ui.state = 0
    ui.save()

    #return render(request, 'fdx_search/search.html',ctx)
    return redirect('search_1', slug11=file_md5)
def search1(request,slug11):
    ctx = {}
    try:
        ui = UploadedImages.objects.get(md5=slug11)
    except:
        return search_error(request,'Поиск не найден')
    ctx['image'] = ui
    image = face_recognition.load_image_file(ui.file.path)
    ctx['face_locations'] = []
    face_locations = face_recognition.face_locations(image)
    faces = len(ctx['face_locations'])
    if faces == 0:
        return search_error(request,'Не удалось найти лица на фото')
    elif faces == 1:
        return redirect('search_1', slug11=ui.md5б slug22=0)
    else:
        cnt = 0
        for top, right, bottom, left in face_locations:
            ctx['face_locations'].append({
                'cnt': cnt,
                'top': top,
                'right': right,
                'bottom': bottom,
                'left':left,
                'width': (right - left),
                'height': (bottom - top)
            })
            cnt = cnt + 1
        faces = len(ctx['face_locations'])
        ui.face_count = faces
        ui.save()
        return render(request, 'fdx_search/search.html',ctx)

def search2(request,slug11,slug22):
    ctx = {}
    return render(request, 'fdx_search/search.html',ctx)