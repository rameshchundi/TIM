from django.urls import path

from . import views

urlpatterns = [
    # /hwrapp/
    path('', views.index, name='index'),
    path('listen_speak',views.listen_speak, name='listen_speak'),
    path('audio_listen',views.audio_listen, name='audio_listen'),
    path('read_speak',views.read_speak, name='read_speak'),
    path('audio_read',views.audio_read, name='audio_read'),
#     path('read_write',views.read_write, name='read_write'),
#     path('upload_read/', views.model_form_upload_read, name='model_form_upload_read'),
#     path('upload_listen/', views.model_form_upload_listen, name='model_form_upload_listen'),
#     path('details_read/<int:image_id>/', views.details_read, name='details_read'),
#     path('details_listen/<int:image_id>/', views.details_listen, name='details_listen'),
#     path('image_read/<int:image_id>', views.image_read, name='image_read'),
#     path('listen_write',views.listen_write, name='listen_write'),
#     path('image_listen/<int:image_id>', views.image_listen, name='image_listen'),


#     # /hwrapp/results/linesegments/image_id
#     path('results/linesegments/<int:image_id>',   
#          views.linesegments, name='linesegments'),
#     # /hwrapp/results/wordsegments/image_id
#     path('results/wordsegments/<int:image_id>',
#          views.wordsegments, name='wordsegments'),
#     # /hwrapp/results/charsegments/image_id
#     path('results/charsegments/<int:image_id>',
#          views.charsegments, name='charsegments'),
#     # /hwrapp/results/augmentation/image_id
#     path('results/augmentation/<int:image_id>',
#          views.augmentation, name='augmentation'),
#     # /hwrapp/upload
#     #path('upload/', views.model_form_upload, name='model_form_upload'),
#     # /hwrapp/delete_image/image_id
#     path('delete_image/<int:image_id>',
#          views.delete_image, name='delete_image'),
   #  path('home', views.home, name='home'),
   # path('comp_audio', views.comp_audio, name='comp_audio'),
   # path('read', views.read, name='read'),
   # path('comp_raudio', views.comp_raudio, name='comp_raudio')
]
