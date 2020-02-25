from django.shortcuts import render
from .models import KanDB
import pygame
import speech_recognition as sr
from difflib import SequenceMatcher
#from django.http import HttpResponse

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Create your views here.
def home(request):

    kandb = KanDB.objects.all()
    #return render(request, 'home.html')
    return render(request, 'home.html', {'kandb': kandb})

def comp_audio(request):

    word=request.POST["word"]
    #res=list(audf)
    #files='../media/audio/1.mp3'
    #d = files + audf
    #pygame.mixer.music.load(files)
    #pygame.mixer.music.play()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Repeat the word:')
        audio = r.listen(source)
        print ('Done!')
    try:
        text = r.recognize_google(audio, language = 'kn-IN')

        if(similar(text,word)>0.74):
            return render(request, 'home.html', {'val': text,'status': 'Successful!'})
        else:
            kandb = KanDB.objects.all()
            return render(request, 'home.html', {'kandb': kandb,'val':text,'stat':'Try Again'})

    except:
        pass

def read(request):
    kandb = KanDB.objects.all()
    return render(request, 'read.html', {'kandb': kandb})

def comp_raudio(request):

    word=request.POST["word"]
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language = 'kn-IN')

        if(similar(text,word)>0.74):
            return render(request, 'read.html', {'val': text,'status': 'Successful!'})
        else:
            kandb = KanDB.objects.all()
            return render(request, 'read.html', {'kandb': kandb,'val':text,'stat':'Try Again'})

    except:
        pass


    #return render(request, 'home.html', {'val': text,'status': 'Successful!', 'form':form})
    #return render(request, 'result.html', {'result':text})