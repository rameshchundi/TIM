from django.http import HttpResponse
from .models import DocumentImage
from django.template import loader
from .models import DocumentImage


import pygame
import speech_recognition as sr
from difflib import SequenceMatcher

from .forms import DocumentForm
#from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import subprocess
import html
# Import module here
import os
import sys

#sys.path.insert(0, 'C:/Users/kevin/Documents/projects/kankali_final/web_app/hwrkannada/kan_db')

from .models import KanDB

count=0

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def index(request):
    return render(request, 'index.html')


# Create your views here.
def listen_speak(request):
    kandb = KanDB.objects.using('postgresql').all()
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'kandb': kandb, 'count': kandb[count]})
    return render(request, 'listen_speak.html', {'kandb': kandb[count]})

def audio_listen(request):
    word=request.POST["word"]
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    
        text = r.recognize_google(audio, language = 'kn-IN')

        if(similar(text,word)>0.9):
            return render(request, 'listen_speak.html', {'val': text,'status': 'Successful!'})
        else:
            kandb = KanDB.objects.using('postgresql').all()
            return render(request, 'listen_speak.html', {'kandb': kandb[count],'val':text,'stat':'Try Again'})

    except:
        kandb = KanDB.objects.using('postgresql').all()
        return render(request, 'listen_speak.html', {'kandb': kandb[count],'val':'','stat':'Adjust the microphone and try again.'})

def read_speak(request):
    kandb = KanDB.objects.using('postgresql').all()
    return render(request, 'read_speak.html', {'kandb': kandb[count]})

def audio_read(request):
    global count
    word=request.POST["word"]
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    
        text = r.recognize_google(audio, language = 'kn-IN')

        if(similar(text,word)>0.9):
            count=count+1
            return render(request, 'read_speak.html', {'val': text,'status': 'Successful!'})
        else:
            kandb = KanDB.objects.using('postgresql').all()
            return render(request, 'read_speak.html', {'kandb': kandb[count],'val':text,'stat':'Try Again'})

    except:
        kandb = KanDB.objects.using('postgresql').all()
        return render(request, 'read_speak.html', {'kandb': kandb[count],'val':'','stat':'Adjust the microphone and try again.'})


# rootdir = ""
# segdir = ""
# augdir = ""
# enddir = ""
# """
#     Index page. Lists last 6 images that were added to database. 
#     Provides option to upload image, the transition between pages(from index to model_form_upload) 
#     happens in html file through <a href> tag
# """


# def read_write(request):
#     if request.method == 'POST':
#         return redirect('/upload_read/')
#     kandb = KanDB.objects.using('postgresql').all()
#     #latest_image_list = DocumentImage.objects.order_by('-pub_date')[:6]
#     template = loader.get_template('read_write.html')
#     #print(latest_image_list)
#     context = {
#         #'latest_image_list': latest_image_list,
#         'kandb': kandb[count],
#     }
#     return HttpResponse(template.render(context, request))


# """
#     Shows the selected image.
#     Provides a button to proceed to analysis of image
# """


# def details_read(request, image_id):
#     if request.method == 'POST':
#          #return redirect('/hwrapp/results/linesegments/' + str(image_id), {
#          #    'image_id': image_id  
#          return redirect('/image_read/' + str(image_id), {
#              'image_id': image_id
#         })

#     template = loader.get_template('details_read.html')
#     #template = loader.get_template('hwrapp/results.html')
#     myobject = DocumentImage.objects.get(pk=image_id)
#     print(myobject)
#     context = {
#         'myobject': myobject,
#         'myobjectid': image_id
#     }
#     return HttpResponse(template.render(context, request))

# def details_listen(request, image_id):
#     if request.method == 'POST':
#          #return redirect('/hwrapp/results/linesegments/' + str(image_id), {
#          #    'image_id': image_id  
#          return redirect('/image_listen/' + str(image_id), {
#              'image_id': image_id
#         })

#     template = loader.get_template('details_listen.html')
#     #template = loader.get_template('hwrapp/results.html')
#     myobject = DocumentImage.objects.get(pk=image_id)
#     print(myobject)
#     context = {
#         'myobject': myobject,
#         'myobjectid': image_id
#     }
#     return HttpResponse(template.render(context, request))


# """
#     A form to upload image from system.
# """


# def model_form_upload_read(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             latest_image = DocumentImage.objects.order_by('-pub_date')[:1]
#             for image in latest_image:
#                 # Use "/" before the path so that the given new path isnt concatenated with present path
#                 return redirect('/details_read/' + str(image.image_id), {
#                     'image_id': image.image_id
#                 })

#     # If form data wasnt valid, display empty form again to the user.
#     else:
#         form = DocumentForm()
#     return render(request, 'model_form_upload_read.html', {
#         'form': form
#     })

# def model_form_upload_listen(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             latest_image = DocumentImage.objects.order_by('-pub_date')[:1]
#             for image in latest_image:
#                 # Use "/" before the path so that the given new path isnt concatenated with present path
#                 return redirect('/details_listen/' + str(image.image_id), {
#                     'image_id': image.image_id
#                 })

#     # If form data wasnt valid, display empty form again to the user.
#     else:
#         form = DocumentForm()
#     return render(request, 'model_form_upload_listen.html', {
#         'form': form
#     })


# def image_read(request, image_id):
#     global rootdir, segdir, enddir
#     kandb = KanDB.objects.using('postgresql').all()
#     myobject = DocumentImage.objects.get(pk=image_id)
#     image_path = myobject.image_url.url
#     image_path = os.path.join(
#         'web_app/hwrkannada/hwrkannada', image_path[1:len(image_path)])

#     path = os.path.join(os.path.dirname(__file__), '../../../')
#     os.chdir(path)
#     sys.path.insert(0, os.getcwd())
#     from main import segmentation_call

#     rootdir, segdir = segmentation_call(image_path)
#     enddir = segdir.split('/images/')[1]
#     imagelist = os.listdir(segdir+"/lines")
#     imagelist.sort()
#     from main import prediction_call,augmentation_call
    
#     augdir = augmentation_call(image_path, segdir)


#     template = loader.get_template('image_read.html')

    

#     output = prediction_call(augdir)
#     # The output is parsed and results page is rendered to show the output
#     output=output[0]
#     output=output.replace(" ", "")
#     #output = ''.join(output.split())
#     h = html.parser.HTMLParser()
#     h.unescape(output)
#     #myobject = DocumentImage.objects.get(pk=image_id)
#     context = {
#         'image_id': image_id,
#         'myobject': myobject,
#         'output': output,
#         'kandb': kandb[count],
#     }
#     return HttpResponse(template.render(context, request))

# def listen_write(request):
#     if request.method == 'POST':
#         return redirect('/upload_listen/')
#     kandb = KanDB.objects.using('postgresql').all()
#     #latest_image_list = DocumentImage.objects.order_by('-pub_date')[:6]
#     template = loader.get_template('listen_write.html')
#     #print(latest_image_list)
#     context = {
#         #'latest_image_list': latest_image_list,
#         'kandb': kandb[count],
#     }
#     return HttpResponse(template.render(context, request))

# def image_listen(request, image_id):
#     global rootdir, segdir, enddir, count
#     kandb = KanDB.objects.using('postgresql').all()
#     myobject = DocumentImage.objects.get(pk=image_id)
#     image_path = myobject.image_url.url
#     image_path = os.path.join(
#         'web_app/hwrkannada/hwrkannada', image_path[1:len(image_path)])

#     path = os.path.join(os.path.dirname(__file__), '../../../')
#     os.chdir(path)
#     sys.path.insert(0, os.getcwd())
#     from main import segmentation_call

#     rootdir, segdir = segmentation_call(image_path)
#     enddir = segdir.split('/images/')[1]
#     imagelist = os.listdir(segdir+"/lines")
#     imagelist.sort()
#     from main import prediction_call,augmentation_call
    
#     augdir = augmentation_call(image_path, segdir)


#     template = loader.get_template('image_listen.html')

    

#     output = prediction_call(augdir)
#     # The output is parsed and results page is rendered to show the output
#     output=output[0]
#     output=output.replace(" ", "")

    

#     h = html.parser.HTMLParser()
#     h.unescape(output)
    
#     #print("op",output)
#     #print("kandb",kandb[count].kannada)
    

#     #myobject = DocumentImage.objects.get(pk=image_id)
#     context = {
#         'image_id': image_id,
#         'myobject': myobject,
#         'output': output,
#         'kandb': kandb[count],
#     }

#     if(output==kandb[count].kannada):
#         print("True")
#         count=count+1

#     return HttpResponse(template.render(context, request))

# """
#     Call for segmentation. Show line segmentation
# """


# def linesegments(request, image_id):
#     global rootdir, segdir, enddir
#     template = loader.get_template('hwrapp/linesegments.html')
#     myobject = DocumentImage.objects.get(pk=image_id)
#     # Image path of selected image which is to be sent to module for processing
#     image_path = myobject.image_url.url
#     """
#          Call script here for segmentation
#     """
#     image_path = os.path.join(
#         'web_app/hwrkannada/hwrkannada', image_path[1:len(image_path)])

#     path = os.path.join(os.path.dirname(__file__), '../../../')
#     os.chdir(path)
#     sys.path.insert(0, os.getcwd())
#     from main import segmentation_call

#     rootdir, segdir = segmentation_call(image_path)
#     enddir = segdir.split('/images/')[1]
#     imagelist = os.listdir(segdir+"/lines")
#     imagelist.sort()
#     context = {
#         'image_id': image_id,
#         'enddir': enddir,
#         'imagelist': imagelist
#     }
#     return HttpResponse(template.render(context, request))


# """
#     Show word segmentation
# """


# def wordsegments(request, image_id):
#     global segdir, enddir
#     template = loader.get_template('hwrapp/wordsegments.html')
#     imagelist = os.listdir(segdir+"/words")
#     imagelist.sort()
#     context = {
#         'image_id': image_id,
#         'enddir': enddir,
#         'imagelist': imagelist
#     }
#     return HttpResponse(template.render(context, request))


# """
#     Character and ottakshara segmentation
# """


# def charsegments(request, image_id):
#     global segdir, enddir
#     template = loader.get_template('hwrapp/charsegments.html')
#     imagelist = []
#     for files in os.listdir(segdir):
#         if os.path.isfile(os.path.join(segdir, files)):
#             imagelist.append(files)
#     imagelist.sort()
#     print(imagelist)
#     context = {
#         'image_id': image_id,
#         'enddir': enddir,
#         'imagelist': imagelist
#     }
#     return HttpResponse(template.render(context, request))


# """
#     Show Augmented characters and ottaksharas
# """


# def augmentation(request, image_id):
#     global rootdir, segdir, augdir
#     template = loader.get_template('hwrapp/augmentation.html')
#     myobject = DocumentImage.objects.get(pk=image_id)
#     # Image path of selected image which is to be sent to module for processing
#     image_path = myobject.image_url.url
#     """
#          Call script here for segmentation
#     """
#     image_path = os.path.join(
#         'web_app/hwrkannada/hwrkannada', image_path[1:len(image_path)])

#     path = os.path.join(os.path.dirname(__file__), '../../../')
#     os.chdir(path)
#     sys.path.insert(0, os.getcwd())
#     from main import augmentation_call

#     augdir = augmentation_call(image_path, segdir)
#     enddir = augdir.split('/images/')[1]
#     imagelist = os.listdir(augdir)
#     imagelist.sort()
#     context = {
#         'image_id': image_id,
#         'enddir': enddir,
#         'imagelist': imagelist
#     }
#     return HttpResponse(template.render(context, request))


# """
#     Result page. Needs to be updated to call our HWR module to analyse image
# """





# def delete_image(request, image_id):
#     image = DocumentImage.objects.get(pk=image_id).delete()
#     return redirect('/hwrapp/')
