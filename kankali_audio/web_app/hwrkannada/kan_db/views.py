from django.shortcuts import render
from .models import KanDB
import pygame
import speech_recognition as sr
from difflib import SequenceMatcher
#from django.http import HttpResponse


count=0

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Create your views here.
def home(request):
    kandb = KanDB.objects.using('postgresql').all()
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'kandb': kandb, 'count': kandb[count]})
    return render(request, 'home.html', {'kandb': kandb[count]})

def comp_audio(request):

    word=request.POST["word"]
    #res=list(audf)
    #files='../media/audio/1.mp3'
    #d = files + audf
    #pygame.mixer.music.load(files)
    #pygame.mixer.music.play()
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    
        text = r.recognize_google(audio, language = 'kn-IN')

        if(similar(text,word)>0.85):
            return render(request, 'home.html', {'val': text,'status': 'Successful!'})
        else:
            kandb = KanDB.objects.using('postgresql').all()
            return render(request, 'home.html', {'kandb': kandb[count],'val':text,'stat':'Try Again'})

    except:
        kandb = KanDB.objects.using('postgresql').all()
        return render(request, 'home.html', {'kandb': kandb[count],'val':'','stat':'Adjust the microphone and try again.'})

def read(request):
    kandb = KanDB.objects.using('postgresql').all()
    return render(request, 'read.html', {'kandb': kandb[count]})

def comp_raudio(request):
    global count
    word=request.POST["word"]
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    
        text = r.recognize_google(audio, language = 'kn-IN')

        if(similar(text,word)>0.85):
            count=count+1
            return render(request, 'read.html', {'val': text,'status': 'Successful!'})
        else:
            kandb = KanDB.objects.using('postgresql').all()
            return render(request, 'read.html', {'kandb': kandb[count],'val':text,'stat':'Try Again'})

    except:
        kandb = KanDB.objects.using('postgresql').all()
        return render(request, 'read.html', {'kandb': kandb[count],'val':'','stat':'Adjust the microphone and try again.'})


    #return render(request, 'home.html', {'val': text,'status': 'Successful!', 'form':form})
    #return render(request, 'result.html', {'result':text})
    #            <!-- {% for kan in kandb|slice:":1" %} -->