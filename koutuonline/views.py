from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
import os
import subprocess
# Create your views here.

supported_format = ['jpg', 'png']
count = 0
folder_path = __file__[:-21]


def cleanUp():
    os.system("rm -f "+folder_path+"/media/img/*")
    os.system("rm -f "+folder_path+"/koutuonline/static/images/*")
    return None


def uploadImg(request):
    globals()['count']+=1
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
                print(folder_path)
                os.system("koutuonline/AlphaMatting-master/main "+folder_path+img1[0].img.url+" "+folder_path+img1[1].img.url+" "+folder_path+\
                      "/koutuonline/static/images/output"+str(globals()['count'])+".png")
                os.system("chmod 666 "+folder_path+"/koutuonline/static/images/output"+str(globals()['count'])+".png")
                os.system("chown nginx "+folder_path+"/koutuonline/static/images/output"+str(globals()['count'])+".png")
                os.system("chgrp nginx "+folder_path+"/koutuonline/static/images/output"+str(globals()['count'])+".png")
                context = {'num':globals()['count']}
                return render(request, 'img_tem/show.html', context)
        except AttributeError:
            return HttpResponseRedirect('/upload')
    else:
        return render(request, 'img_tem/upload.html')


def uploadImg2(request):
    globals()['count']+=1
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
                    'imgs': globals()['count'],
                }
                # os.system("chown nginx "+folder_path+new_img.img.url)
                # os.system("chgrp nginx "+folder_path+new_img.img.url)
                # os.system("chmod 666 "+folder_path+new_img.img.url)
                print("cp "+folder_path+new_img.img.url+" "+folder_path+"/koutuonline/static/images/paint"+str(globals()['count'])+".png")
                os.system("cp "+folder_path+new_img.img.url+" "+folder_path+"/koutuonline/static/images/paint"+str(globals()['count'])+".png")
                os.system("chown nginx "+folder_path+"/koutuonline/static/images/paint"+str(globals()['count'])+".png")
                os.system("chgrp nginx "+folder_path+"/koutuonline/static/images/paint"+str(globals()['count'])+".png")
                os.system("chmod 666 "+folder_path+"/koutuonline/static/images/paint"+str(globals()['count'])+".png")
                return render(request, 'img_tem/paint.html', content)
        except AttributeError:
            return render(request, 'img_tem/upload-editor.html')
    else:
        return render(request, 'img_tem/upload-editor.html')
