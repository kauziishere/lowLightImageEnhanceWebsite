from django.shortcuts import render
from lowLightImageEnhancement.forms import *
from lowLightImageEnhancement.models import *
from lowLightImageEnhancement.custom_test import *
# Create your views here.
def saveImage(request):
    saved = False
    post = {}
    if request.method == "POST":
        object = form(request.POST, request.FILES)
        if object.is_valid():
            image = object.cleaned_data["image"]
            if(str(image)[-3:] != "ARW"):
                post['error_message'] = "Incorrect image format"
                return render(request,  'lowLightImageEnhancement/basePage.html', post)
            saved = custom_test(image)
            if(saved == True):
                post['out'] = 'out.png'
    if(saved == False):
        return render(request, 'lowLightImageEnhancement/basePage.html', post)
    return render(request, 'lowLightImageEnhancement/base.html', post)
