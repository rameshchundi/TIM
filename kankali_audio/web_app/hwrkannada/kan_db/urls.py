from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('comp_audio', views.comp_audio, name='comp_audio'),
    path('read', views.read, name='read'),
    path('comp_raudio', views.comp_raudio, name='comp_raudio')
]