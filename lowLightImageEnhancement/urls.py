from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
   path('',views.saveImage, name = 'saveImage'),
   path('saved', views.saveImage, name = 'saved')
]
