from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
import os
# Create your views here.

supported_format = ['jpg', 'png']

def uploadImg(request):
    if request.method == 'POST':
        try:
            new_img = IMG(
                img=request.FILES.get('img'),
                name=request.FILES.get('img').name
            )
            new_img_gray = IMG(
                img=request.FILES.get('img-gray'),
                name=request.FILES.get('img-gray').name
            )
            if (new_img.name[-3:].lower() not in supported_format) or (
                    new_img_gray.name[-3:].lower() not in supported_format):
                return HttpResponseRedirect('/upload')
            else:
                new_img.save()
                new_img_gray.save()
                img1 = GetAll()[-2:]
                folder_path = __file__[:-21]
                print(folder_path)
                print("koutuonline/AlphaMatting-master/main "+folder_path+img1[0].img.url+" "+folder_path+img1[1].img.url+" "+folder_path+\
                      "/koutuonline/static/images/output.png")
                os.system("koutuonline/AlphaMatting-master/main "+folder_path+img1[0].img.url+" "+folder_path+img1[1].img.url+" "+folder_path+\
                      "/koutuonline/static/images/output.png")
            return render(request, 'img_tem/show.html')
        except AttributeError:
            return HttpResponseRedirect('/upload')
    else:
        return render(request, 'img_tem/upload.html')


def uploadImg2(request):
    if request.method == 'POST':
        try:
            new_img = IMG(
                img=request.FILES.get('img'),
                name=request.FILES.get('img').name
            )
            if new_img.name[-3:].lower() not in supported_format:
                return render(request, 'img_tem/upload-editor.html')
            else:
                new_img.save()
                print(new_img.img.url)
                content={
                    'imgs':new_img,
                }
                return render(request, 'img_tem/paint.html', content)
        except AttributeError:
            return render(request, 'img_tem/upload-editor.html')
    else:
        return render(request, 'img_tem/upload-editor.html')


def uploadImg3(request):
    if request.method == 'POST':
        try:
            new_img = IMG(
                img=request.FILES.get('img'),
                name=request.FILES.get('img').name
            )
            new_img_gray = IMG(
                img=request.FILES.get('img-gray'),
                name=request.FILES.get('img-gray').name
            )
            if (new_img.name[-3:].lower() not in supported_format) or (
                    new_img_gray.name[-3:].lower() not in supported_format):
                return HttpResponseRedirect('/scribble')
            else:

                new_img.save()
                new_img_gray.save()
                img1 = GetAll()[-2:]
                folder_path = __file__[:-21]
                print(folder_path)
                print("python3 koutuonline/closed-form-matting-master/closed_form_matting.py "+folder_path+img1[0].img.url+" -s "+folder_path+img1[1].img.url+" -o "+folder_path+\
                      "/koutuonline/static/images/output.png")
                os.system("python3 koutuonline/closed-form-matting-master/closed_form_matting.py "+folder_path+img1[0].img.url+" -s "+folder_path+img1[1].img.url+" -o "+folder_path+\
                      "/koutuonline/static/images/output.png")
            return render(request, 'img_tem/show.html')
        except AttributeError:
            return HttpResponseRedirect('/scribble')
    else:
        return render(request, 'img_tem/upload-scribble.html')

