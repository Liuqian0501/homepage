from django.urls import path

from . import views

urlpatterns = [
    path('soulpainting', views.styleTransform, name='styleTransform'),
    path('recognition', views.recognition, name='recognition'),
]