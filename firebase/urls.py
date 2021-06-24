from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('push', views.push, name='push'),
    path('set', views.set, name='set'),
    path('update', views.update, name='update'),
    path('updateMutilLocation', views.updateMutilLocation, name='updateMutilLocation'),
    path('updateMutilLocationWithGenerateKey', views.updateMutilLocationWithGenerateKey, name='updateMutilLocationWithGenerateKey'),
    path('uploadImage', views.uploadImage, name='uploadImage'),
]
